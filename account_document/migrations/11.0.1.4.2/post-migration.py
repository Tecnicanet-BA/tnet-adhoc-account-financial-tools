from openupgradelib import openupgrade
import logging

_logger = logging.getLogger(__name__)


@openupgrade.migrate()
def migrate(env, version):

    _logger.info('Update account.document.type to noupdate=True')
    items = env['ir.model.data'].search([
        ('model', '=', 'account.document.type'),
        ('module', '=', 'account_document'),
    ])
    items = items.write({'noupdate': True})
