# © 2019 Numigi (tm) and all its contributors (https://bit.ly/numigiens)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    'name': 'Project Template / Timesheet',
    'version': '1.0.0',
    'author': 'Numigi',
    'maintainer': 'Numigi',
    'license': 'LGPL-3',
    'category': 'Project',
    'summary': 'Binding between project_template_numigi and hr_timesheet',
    'depends': [
        'project_template_numigi',
        'hr_timesheet',
    ],
    'data': [
        'views/project_task.xml',
    ],
    'installable': True,
    'auto_install': False,
}
