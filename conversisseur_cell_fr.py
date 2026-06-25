import panel as pn

pn.extension()

temp = pn.widgets.FloatInput(name="Température", value=0)

unit = pn.widgets.RadioButtonGroup(
    name="Unité",
    options=["Celsius", "Fahrenheit", "Kelvin"],
    button_type="primary"
)

result = pn.pane.Markdown("")

def convert(event):
    value = temp.value
    u = unit.value

    if u == "Celsius":
        c = value
    elif u == "Fahrenheit":
        c = (value - 32) * 5/9
    else:
        c = value - 273.15

    f = (c * 9/5) + 32
    k = c + 273.15

    result.object = f"""
- Celsius: {c:.2f} °C
- Fahrenheit: {f:.2f} °F
- Kelvin: {k:.2f} K
"""

button = pn.widgets.Button(name="Convertir", button_type="success")
button.on_click(convert)

pn.Column(
    "## Convertisseur",
    temp,
    unit,
    button,
    result
).servable()