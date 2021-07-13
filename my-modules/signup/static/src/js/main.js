odoo.define('signup.main', function (require) {
    'use strict';


    var publicWidget = require('web.public.widget');


    publicWidget.registry.AuthSignupHome = publicWidget.Widget.extend({
        selector: '#o_birthday',
        start: function () {
            var self = this;

            $('.custom-datepicker').datepicker({
                autoclose: true,
                format: "yyyy-mm-dd",
                changeMonth: true,
                changeYear: true,
                language: "es",


            });


        },


    })
});
