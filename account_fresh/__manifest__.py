{
    'name': 'account invoice addons',
    'description': 'account invoice addons',
    'author': '1di0t',
    'depends': ['base',
                'account',
                'hr_expense',
                'product',
                'purchase',
                'sale',
                'osbzr_account',
                'fleet',
                'account_hierarchy',
                'account_period',
                'l10n_cn_voucher',
                'stock_account2'],
    'application': True,
    'data': [
        'security/account_security.xml',
        'security/ir.model.access.csv',
        'views/account_invoice.xml',
        'views/account_payment.xml',
        'views/hr_expense_payment.xml',
        # 'views/product_strategy.xml',
        'views/purchase.xml',
        'views/sale.xml',
        # 'views/stock_quant.xml',
        'views/hr_expense.xml',
        'views/stock_pack_operation.xml',
        'views/res_company.xml',
        'views/stock_picking.xml',
        'views/actual_invoice_view.xml',
        'views/stock_move.xml',
        'views/fleet_vehicle.xml'
    ],
}
