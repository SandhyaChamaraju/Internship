letter_template='''Dear <|Name|>,
You are selected!
<|Date|>'''

name_input="Sandhya"
date_input="August 20,2026"

filled_letter=letter_template.replace("<|Name|>", name_input)
filled_letter=filled_letter.replace("<|Date|>", date_input)

print(filled_letter)
