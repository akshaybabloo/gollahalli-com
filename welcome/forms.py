#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2016 Akshay Raj Gollahalli

import operator

from django import forms

from .models import AbiesModel

COUNTRY_LIST = {"AF": "Afghanistan", "AX": "\u00c5land Islands", "AL": "Albania", "DZ": "Algeria",
                "AS": "American Samoa", "AD": "Andorra", "AO": "Angola", "AI": "Anguilla", "AQ": "Antarctica",
                "AG": "Antigua & Barbuda", "AR": "Argentina", "AM": "Armenia", "AW": "Aruba", "AC": "Ascension Island",
                "AU": "Australia", "AT": "Austria", "AZ": "Azerbaijan", "BS": "Bahamas", "BH": "Bahrain",
                "BD": "Bangladesh", "BB": "Barbados", "BY": "Belarus", "BE": "Belgium", "BZ": "Belize", "BJ": "Benin",
                "BM": "Bermuda", "BT": "Bhutan", "BO": "Bolivia", "BA": "Bosnia & Herzegovina", "BW": "Botswana",
                "BR": "Brazil", "IO": "British Indian Ocean Territory", "VG": "British Virgin Islands", "BN": "Brunei",
                "BG": "Bulgaria", "BF": "Burkina Faso", "BI": "Burundi", "KH": "Cambodia", "CM": "Cameroon",
                "CA": "Canada", "IC": "Canary Islands", "CV": "Cape Verde", "BQ": "Caribbean Netherlands",
                "KY": "Cayman Islands", "CF": "Central African Republic", "EA": "Ceuta & Melilla", "TD": "Chad",
                "CL": "Chile", "CN": "China", "CX": "Christmas Island", "CC": "Cocos (Keeling) Islands",
                "CO": "Colombia", "KM": "Comoros", "CG": "Congo - Brazzaville", "CD": "Congo - Kinshasa",
                "CK": "Cook Islands", "CR": "Costa Rica", "CI": "C\u00f4te d\u2019Ivoire", "HR": "Croatia",
                "CU": "Cuba", "CW": "Cura\u00e7ao", "CY": "Cyprus", "CZ": "Czech Republic", "DK": "Denmark",
                "DG": "Diego Garcia", "DJ": "Djibouti", "DM": "Dominica", "DO": "Dominican Republic", "EC": "Ecuador",
                "EG": "Egypt", "SV": "El Salvador", "GQ": "Equatorial Guinea", "ER": "Eritrea", "EE": "Estonia",
                "ET": "Ethiopia", "FK": "Falkland Islands", "FO": "Faroe Islands", "FJ": "Fiji", "FI": "Finland",
                "FR": "France", "GF": "French Guiana", "PF": "French Polynesia", "TF": "French Southern Territories",
                "GA": "Gabon", "GM": "Gambia", "GE": "Georgia", "DE": "Germany", "GH": "Ghana", "GI": "Gibraltar",
                "GR": "Greece", "GL": "Greenland", "GD": "Grenada", "GP": "Guadeloupe", "GU": "Guam", "GT": "Guatemala",
                "GG": "Guernsey", "GN": "Guinea", "GW": "Guinea-Bissau", "GY": "Guyana", "HT": "Haiti",
                "HN": "Honduras", "HK": "Hong Kong SAR China", "HU": "Hungary", "IS": "Iceland", "IN": "India",
                "ID": "Indonesia", "IR": "Iran", "IQ": "Iraq", "IE": "Ireland", "IM": "Isle of Man", "IL": "Israel",
                "IT": "Italy", "JM": "Jamaica", "JP": "Japan", "JE": "Jersey", "JO": "Jordan", "KZ": "Kazakhstan",
                "KE": "Kenya", "KI": "Kiribati", "XK": "Kosovo", "KW": "Kuwait", "KG": "Kyrgyzstan", "LA": "Laos",
                "LV": "Latvia", "LB": "Lebanon", "LS": "Lesotho", "LR": "Liberia", "LY": "Libya", "LI": "Liechtenstein",
                "LT": "Lithuania", "LU": "Luxembourg", "MO": "Macau SAR China", "MK": "Macedonia", "MG": "Madagascar",
                "MW": "Malawi", "MY": "Malaysia", "MV": "Maldives", "ML": "Mali", "MT": "Malta",
                "MH": "Marshall Islands", "MQ": "Martinique", "MR": "Mauritania", "MU": "Mauritius", "YT": "Mayotte",
                "MX": "Mexico", "FM": "Micronesia", "MD": "Moldova", "MC": "Monaco", "MN": "Mongolia",
                "ME": "Montenegro", "MS": "Montserrat", "MA": "Morocco", "MZ": "Mozambique", "MM": "Myanmar (Burma)",
                "NA": "Namibia", "NR": "Nauru", "NP": "Nepal", "NL": "Netherlands", "NC": "New Caledonia",
                "NZ": "New Zealand", "NI": "Nicaragua", "NE": "Niger", "NG": "Nigeria", "NU": "Niue",
                "NF": "Norfolk Island", "KP": "North Korea", "MP": "Northern Mariana Islands", "NO": "Norway",
                "OM": "Oman", "PK": "Pakistan", "PW": "Palau", "PS": "Palestinian Territories", "PA": "Panama",
                "PG": "Papua New Guinea", "PY": "Paraguay", "PE": "Peru", "PH": "Philippines", "PN": "Pitcairn Islands",
                "PL": "Poland", "PT": "Portugal", "PR": "Puerto Rico", "QA": "Qatar", "RE": "R\u00e9union",
                "RO": "Romania", "RU": "Russia", "RW": "Rwanda", "WS": "Samoa", "SM": "San Marino",
                "ST": "S\u00e3o Tom\u00e9 & Pr\u00edncipe", "SA": "Saudi Arabia", "SN": "Senegal", "RS": "Serbia",
                "SC": "Seychelles", "SL": "Sierra Leone", "SG": "Singapore", "SX": "Sint Maarten", "SK": "Slovakia",
                "SI": "Slovenia", "SB": "Solomon Islands", "SO": "Somalia", "ZA": "South Africa",
                "GS": "South Georgia & South Sandwich Islands", "KR": "South Korea", "SS": "South Sudan", "ES": "Spain",
                "LK": "Sri Lanka", "BL": "St. Barth\u00e9lemy", "SH": "St. Helena", "KN": "St. Kitts & Nevis",
                "LC": "St. Lucia", "MF": "St. Martin", "PM": "St. Pierre & Miquelon", "VC": "St. Vincent & Grenadines",
                "SD": "Sudan", "SR": "Suriname", "SJ": "Svalbard & Jan Mayen", "SZ": "Swaziland", "SE": "Sweden",
                "CH": "Switzerland", "SY": "Syria", "TW": "Taiwan", "TJ": "Tajikistan", "TZ": "Tanzania",
                "TH": "Thailand", "TL": "Timor-Leste", "TG": "Togo", "TK": "Tokelau", "TO": "Tonga",
                "TT": "Trinidad & Tobago", "TA": "Tristan da Cunha", "TN": "Tunisia", "TR": "Turkey",
                "TM": "Turkmenistan", "TC": "Turks & Caicos Islands", "TV": "Tuvalu", "UM": "U.S. Outlying Islands",
                "VI": "U.S. Virgin Islands", "UG": "Uganda", "UA": "Ukraine", "AE": "United Arab Emirates",
                "GB": "United Kingdom", "US": "United States", "UY": "Uruguay", "UZ": "Uzbekistan", "VU": "Vanuatu",
                "VA": "Vatican City", "VE": "Venezuela", "VN": "Vietnam", "WF": "Wallis & Futuna",
                "EH": "Western Sahara", "YE": "Yemen", "ZM": "Zambia", "ZW": "Zimbabwe"}


class WelcomeForm(forms.Form):
    # page 1
    first_name = forms.CharField(max_length=120, required=False)
    last_name = forms.CharField(max_length=120, required=False)
    profile_image_location = forms.ImageField(required=False)
    email = forms.EmailField(required=False)

    # page 2
    username = forms.CharField(max_length=120, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)
    # AWS_SECRET = forms.CharField(max_length=120)
    # AWS_SECRET_KEY = forms.CharField(widget=forms.PasswordInput)
    # AWS_S3_BUCKET_NAME = forms.CharField(max_length=120)

    # page 3
    company_name = forms.CharField(max_length=240, required=False)
    company_logo_location = forms.ImageField(required=False)
    city = forms.CharField(max_length=120, required=False)
    country = forms.CharField(max_length=120, required=False)
    # country = forms.ChoiceField(choices=COUNTRY_LIST, label=u'Country')


class WelcomeFormModel(forms.ModelForm):
    class Meta:
        model = AbiesModel
        fields = ('first_name', 'last_name', 'profile_image_location', 'email', 'username', 'password', 'company_name',
                  'company_logo_location', 'city', 'country')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_image_location': forms.FileInput(attrs={'class': 'form-control', 'id': 'wizard-picture'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'company_logo_location': forms.FileInput(attrs={'class': 'form-control'}),
            'country': forms.Select(choices=list(sorted(COUNTRY_LIST.items(), key=operator.itemgetter(1))),
                                    attrs={'class': 'form-control'})
        }
