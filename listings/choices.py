
# iterate over choises
# to show as html options
# turn the options fields into a python dictionary
"""
<div class="col-md-4 mb-3">
<label class="sr-only">State</label>
<select name="state" class="form-control">
    <option selected="true" disabled="disabled">State (All)</option>
    <option value="AL">Alabama</option>
    <option value="AK">Alaska</option>
    <option value="AZ">Arizona</option>
    <option value="AR">Arkansas</option>
etc...
"""

"""
<div class="form-row">
    <div class="col-md-6 mb-3">
        <label class="sr-only">Bedrooms</label>
        <select name="bedrooms" class="form-control">
            <option selected="true" disabled="disabled">Bedrooms (All)</option>
            <option value="1">1</option>
            <option value="2">2</option>
            <option value="3">3</option>
etc...
    <div class="col-md-6 mb-3">
        <select name="price" class="form-control" id="type">
            <option selected="true" disabled="disabled">Max Price (Any)</option>
            <option value="100000">$100,000</option>
            <option value="200000">$200,000</option>
            <option value="300000">$300,000</option>
etc...
"""

# state_choices
state_choices = {
    'AL':'Alabama',
    'AK':'Alaska',
    'AZ':'Arizona',
    'AR':'Arkansas',
    'CA':'California',
    'CO':'Colorado',
    'CT':'Connecticut',
    'DE':'Delaware',
    'DC':'District Of Columbia',
    'FL':'Florida',
    'GA':'Georgia',
    'HI':'Hawaii',
    'ID':'Idaho',
    'IL':'Illinois',
    'IN':'Indiana',
    'IA':'Iowa',
    'KS':'Kansas',
    'KY':'Kentucky',
    'LA':'Louisiana',
    'ME':'Maine',
    'MD':'Maryland',
    'MA':'Massachusetts',
    'MI':'Michigan',
    'MN':'Minnesota',
    'MS':'Mississippi',
    'MO':'Missouri',
    'MT':'Montana',
    'NE':'Nebraska',
    'NV':'Nevada',
    'NH':'New Hampshire',
    'NJ':'New Jersey',
    'NM':'New Mexico',
    'NY':'New York',
    'NC':'North Carolina',
    'ND':'North Dakota',
    'OH':'Ohio',
    'OK':'Oklahoma',
    'OR':'Oregon',
    'PA':'Pennsylvania',
    'RI':'Rhode Island',
    'SC':'South Carolina',
    'SD':'South Dakota',
    'TN':'Tennessee',
    'TX':'Texas',
    'UT':'Utah',
    'VT':'Vermont',
    'VA':'Virginia',
    'WA':'Washington',
    'WV':'West Virginia',
    'WI':'Wisconsin',
    'WY':'Wyoming'
}

# bedroom_choices
bedroom_choices = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    '10':10
}

# price_choices
price_choices = {
    '100000':'$100,000',
    '200000':'$200,000',
    '300000':'$300,000',
    '400000':'$400,000',
    '500000':'$500,000',
    '600000':'$600,000',
    '700000':'$700,000',
    '800000':'$800,000',
    '900000':'$900,000',
    '1000000':'$1M+'
}

