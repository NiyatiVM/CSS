/*
 * Require jQuery
 */
var SliderCaptcha = function(element, options) {
    // Object Composition
    this.data = {
        options: $.extend({
            authValue: 'Authenticated!',
            cursor: 'move',
            customValidation: true,
            direction: 'x', //x or y
            handle: '.handle',
            hintText: 'Grab and Slide',
            inputName: 'captcha',
            completeCallback: defaultCompleteCallback
        }, options),
        handle: {
            obj: 0,
            active: 0,
            oWidth: 0
        },
        slide: {
            obj: $(element),
            width: 0,
            oWidth: 0
        },
        form: {
            obj: 0,
            input: 0
        }
    };

    // Object data alias : It's a relics, maybe future removed
    this.options = this.data.options;
    this.handle = this.data.handle;
    this.slide = this.data.slide;
    this.form = this.data.form;

    this.init = function () {
        // Init data
        this.slide.obj = $(element);
        this.slide.obj.addClass('slide-to-captcha');
        this.slide.width = this.slide.obj.width();
        this.slide.oWidth = this.slide.obj.outerWidth(true);

        /* Slider Logic
         *    --------------------
         *   |   _                |
         *   |  |_|-------------  |
         *   |                    |
         *    --------------------
         *      |--------------|
         *
         * start = slide.left + (slide.oWidth - slide.width) / 2;
         * end   = (start + )slide.width - handle.width/2
         *         ^ this practically not necessary, I don't know
         * handleCenterPos = e.pageX - handle.width/2
         */
        this.slide.start = this.slide.obj.offset().left + (this.slide.oWidth - this.slide.width) / 2;
        this.slide.end = this.slide.start + this.slide.width;

        // Show hint
        $('.slide-to-captcha').attr('data-content', this.options.hintText);

        this.handle.obj = $(element).find(this.options.handle);
        this.handle.obj.addClass('slide-to-captcha-handle');
        this.handle.obj.offset({ left: this.slide.start });
        this.handle.width = this.handle.obj.width();
        this.handle.oWidth = this.handle.obj.outerWidth();
        // Substract half of the handle width from the track width
        this.slide.end = this.slide.end - (this.handle.width / 2);

        // console.log("start %i = %i + (%i - %i) / 2", this.slide.start, this.slide.obj.offset().left, this.slide.oWidth, this.slide.width);
        // console.log("end   %i = %i - (%i / 2)", this.slide.end, this.slide.width, this.handle.width);

        this.form.obj = this.slide.obj.parents('form');

        this.form.input = $(this.form.obj).find('input[name=' + this.options.inputName + ']');

        if (this.options.customValidation === false) {
            this.form.obj.attr('data-valid', 'false');
            this.form.obj.attr('onsubmit', "return $(this).attr('data-valid') === 'true';");
        }

        this.handle.obj.css('cursor', this.options.cursor)
            .on('mousedown', this, this.onDrag);

    };

    this.destroy = function () {
        this.form.obj.removeAttr('data-valid', 'false');

        this.handle.obj.removeClass('slide-to-captcha-handle');
        this.slide.obj.removeClass('slide-to-captcha');
        this.slide.obj.removeClass('valid');

        this.form.input.attr('value', '');

        this.handle.obj.css('cursor', 'normal')
            .on('mousedown', null);

        this.handle.active.offset({left: 0});
    };

    this.reset = function () {
        this.destroy();
        this.init();
    };

    this.onDrag = function (e) {
        var data = e.data;

        data.handle.active = $(this).addClass('active-handle');

        data.handle.obj
            .on('mousemove', data, data.onMove)
            .on('mouseup', data, data.onRelease);
        // if(data.options.direction === 'y') {
        //    yPos = handle.offset().top + handleHeight = e.pageY;
        // }

        // To avoid calculation error when style doesn't fully loaded,
        // recalc slider start and end here
        data.slide.start = data.slide.obj.offset().left + (data.slide.oWidth - data.slide.width) / 2;
        data.slide.end = data.slide.start + data.slide.width - data.handle.width;

        e.preventDefault();

    };

    this.onMove = function (e) {
        var data = e.data;

        var handleXPos = data.handle.obj.offset().left + (e.pageX - data.handle.obj.offset().left - (data.handle.width / 2));

        console.log('pageX: %i . handle off: %i', e.pageX, data.handle.obj.offset().left);
        // console.log('%i > %i or < %i', handleXPos, data.slide.start, data.slide.end);
        if(handleXPos >= data.slide.start && handleXPos <= data.slide.end) {
            // console.log(handleXPos - data.slide.start);
            if (data.handle.obj.hasClass('active-handle')) {
                data.handle.active.offset({left: handleXPos});
            }
        } else {
            // console.log('%i >= %i ?', handleXPos, data.slide.end);
            if(handleXPos >= data.slide.end) {
                var ev = { data: data };
                data.onComplete(ev);
            }
            data.handle.active.mouseup();
        }
    };

    this.onComplete = function (e) {
        var data = e.data;

        data.handle.active.offset({ left: data.slide.end });
        data.handle.active.off();
        data.onRelease(e);
        data.form.obj.attr('data-valid', 'true');
        data.slide.obj.addClass('valid');
        data.options.completeCallback(data);

        data.form.input.attr('value', data.options.authValue);
    };

    function defaultCompleteCallback(data) {
        console.log('Authenticated as human!');
        data.slide.obj.attr('data-content', data.options.authValue);
    };

    this.onRelease = function (e) {
        var data = e.data;
        data.handle.active.removeClass('active-handle');
    };

    // Solo function
    this.init();
};
