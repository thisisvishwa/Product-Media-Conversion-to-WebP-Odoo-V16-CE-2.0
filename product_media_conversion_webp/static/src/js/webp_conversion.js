odoo.define('product_media_conversion_webp.webp_conversion', function (require) {
    "use strict";

    var ajax = require('web.ajax');
    var core = require('web.core');
    var Widget = require('web.Widget');
    var Dialog = require('web.Dialog');

    var _t = core._t;

    var WebPConversionSettings = Widget.extend({
        template: 'WebPConversionSettingsTemplate',
        events: {
            'click .js_apply_settings': '_onApplySettings',
        },

        init: function (parent, options) {
            this._super(parent);
            this.options = _.extend(options || {}, {
                quality: 80,
                optimizationLevel: 2,
                enabled: true
            });
        },

        start: function () {
            var self = this;
            this._loadSettings().then(function (settings) {
                self.options = settings;
                self._render();
            });
            return this._super();
        },

        _loadSettings: function () {
            return ajax.jsonRpc('/webp_conversion/settings/get', 'call', {})
                .then(function (settings) {
                    return settings;
                });
        },

        _render: function () {
            this.$('.js_quality').val(this.options.quality);
            this.$('.js_optimization_level').val(this.options.optimizationLevel);
            this.$('.js_enabled').prop('checked', this.options.enabled);
        },

        _onApplySettings: function () {
            var settings = {
                quality: parseInt(this.$('.js_quality').val(), 10),
                optimizationLevel: parseInt(this.$('.js_optimization_level').val(), 10),
                enabled: this.$('.js_enabled').is(':checked')
            };

            ajax.jsonRpc('/webp_conversion/settings/set', 'call', settings)
                .then(function (result) {
                    if (result.success) {
                        Dialog.alert(this, _t("Settings saved successfully!"), {
                            title: _t("Success"),
                        });
                    } else {
                        Dialog.alert(this, _t("Failed to save settings."), {
                            title: _t("Error"),
                        });
                    }
                }.bind(this));
        }
    });

    var WebPConversionErrorHandler = Widget.extend({
        template: 'WebPErrorLogTemplate',
        events: {
            'click .js_export_logs': '_onExportLogs',
        },

        init: function (parent, options) {
            this._super(parent);
            this.options = options || {};
        },

        start: function () {
            this._loadErrorLogs();
            return this._super();
        },

        _loadErrorLogs: function () {
            var self = this;
            ajax.jsonRpc('/webp_conversion/error_logs/get', 'call', {})
                .then(function (logs) {
                    self.$('.js_error_logs').html(logs);
                });
        },

        _onExportLogs: function () {
            window.location = '/webp_conversion/error_logs/export';
        }
    });

    core.action_registry.add('webp_conversion_settings', WebPConversionSettings);
    core.action_registry.add('webp_conversion_error_handler', WebPConversionErrorHandler);

    return {
        WebPConversionSettings: WebPConversionSettings,
        WebPConversionErrorHandler: WebPConversionErrorHandler,
    };
});