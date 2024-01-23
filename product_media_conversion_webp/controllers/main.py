from odoo import http, fields, models
from odoo.http import request
import logging
import base64
from PIL import Image
import io

_logger = logging.getLogger(__name__)

class ProductMediaConversionWebPController(http.Controller):

    @http.route('/webp_conversion/convert', type='json', auth="user")
    def convert_to_webp(self, image_id):
        image_record = request.env['product.image'].browse(image_id)
        if image_record:
            try:
                image_stream = io.BytesIO(base64.b64decode(image_record.image))
                image = Image.open(image_stream)
                if image.format in ['PNG', 'JPEG', 'JPG']:
                    output_stream = io.BytesIO()
                    image.save(output_stream, format='WEBP')
                    webp_image = base64.b64encode(output_stream.getvalue())
                    image_record.write({'image': webp_image})
                    return {'status': 'success', 'message': 'Image converted to WebP format.'}
                else:
                    return {'status': 'error', 'message': 'Unsupported image format.'}
            except Exception as e:
                _logger.exception("Error converting image to WebP: %s", e)
                request.env['webp.conversion.error'].create({
                    'error_type': str(e),
                    'timestamp': fields.Datetime.now(),
                    'affected_image': image_record.id
                })
                return {'status': 'error', 'message': 'Error occurred during conversion.'}
        else:
            return {'status': 'error', 'message': 'Image not found.'}

    @http.route('/webp_conversion/settings', type='json', auth="user")
    def get_conversion_settings(self):
        settings = request.env['res.config.settings'].search([], limit=1)
        return {
            'enabled': settings.webp_conversion_enabled,
            'optimization_level': settings.webp_optimization_level,
            'quality': settings.webp_quality
        }

    @http.route('/webp_conversion/error_logs', type='http', auth="user")
    def get_error_logs(self):
        error_logs = request.env['webp.conversion.error'].search([])
        return request.render('product_media_conversion_webp.webp_conversion_error_views', {
            'error_logs': error_logs
        })