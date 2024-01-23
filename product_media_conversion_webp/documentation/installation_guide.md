# Product Media Conversion to WebP Module Installation Guide

## Prerequisites
Before you begin the installation of the Product Media Conversion to WebP Module, ensure that you have the following:
- Odoo 16 Community Edition installed and running.
- Administrative access to the Odoo backend.
- The module `website_sale` installed as it is a dependency for this module.

## Installation Steps

1. **Download the Module:**
   - Navigate to [https://thisis.com](https://thisis.com) and download the `product_media_conversion_webp` module.

2. **Add the Module to Odoo Addons Path:**
   - Place the downloaded `product_media_conversion_webp` folder into your Odoo addons directory. The default path is usually `/odoo/addons`.

3. **Update Module List:**
   - Log in to your Odoo backend with administrative credentials.
   - Navigate to `Apps` menu without applying any filters.
   - Click on `Update Apps List` from the top-right corner. Confirm the action if prompted.

4. **Install the Module:**
   - In the Apps menu, search for `Product Media Conversion to WebP`.
   - When the module appears, click on the `Install` button.

5. **Verify Installation:**
   - After the installation process is complete, you should see the module listed as installed in the Apps menu.
   - Additionally, you can navigate to `Settings` > `Technical` > `Modules` and search for `product_media_conversion_webp` to ensure it is installed.

## Post-Installation Configuration

1. **Configure Image Conversion Settings:**
   - Go to `Settings` and look for the `Product Media Conversion to WebP` section.
   - Click on `Manage Conversion Settings` to open the configuration interface.
   - Here you can enable/disable the conversion feature, configure optimization settings, and define supported image formats.

2. **Schedule Automatic Conversion (Optional):**
   - Navigate to `Settings` > `Technical` > `Automation` > `Scheduled Actions`.
   - Look for the `ir_cron_image_conversion_job` and ensure it is active.
   - You can adjust the frequency and timing of the scheduled job as per your requirements.

## Troubleshooting

If you encounter any issues during the installation or configuration, please refer to the `troubleshooting_guide.md` provided with the module for common problems and solutions.

For further assistance, you can also reach out to the module author through the support channels listed on [https://thisis.com](https://thisis.com).

Thank you for choosing the Product Media Conversion to WebP Module for Odoo 16 Community Edition. We hope it enhances your website's performance and user experience.