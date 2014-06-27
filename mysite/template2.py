from django.template import Template, Context
raw_template = """<p>Dear {{ person_name }},</p>

<p>Thanks for ordering {{ product }} from {{ company }}. It's scheduled
to ship on {{ ship_date|date:"F j, Y" }}.</p>

{% if ordered_warranty %}
<p>Your warranty information will be included in the packaging.</p>
{% endif %}
<p>Sincerely,<br />{{ company }}</p>"""
t = Template(raw_template)
import datetime
c = Context({'person_name': 'John Smith',
    'product': 'Super Lawn Mower',
    'company': 'Outdoor Equipment',
    'ship_date': datetime.date(2009, 4, 2),
    'ordered_warranty': True})
t.render(c)

#RESULTADO
"<p>Dear John Smith,</p>\n\n<p>Thanks for ordering Super Lawn Mower from
Outdoor Equipment. It's scheduled \nto ship on April 2, 2009.</p>\n\n\n
<p>Your warranty information will be included in the packaging.</p>\n\n\n
<p>Sincerely,<br />Outdoor Equipment</p>"

'''	Estos son los fundamentos del uso del sistema de plantillas 
	de Django: sólo escribe una plantilla, crea un objeto Template,
	crea un Context, y llama al método render().
'''