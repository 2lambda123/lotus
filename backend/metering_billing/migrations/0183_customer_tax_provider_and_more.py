# Generated by Django 4.0.5 on 2023-02-16 20:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import metering_billing.utils.utils


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0182_guard_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="tax_provider",
            field=models.PositiveSmallIntegerField(
                blank=True, choices=[(1, "taxjar"), (2, "lotus")], null=True
            ),
        ),
        migrations.AddField(
            model_name="historicalcustomer",
            name="tax_provider",
            field=models.PositiveSmallIntegerField(
                blank=True, choices=[(1, "taxjar"), (2, "lotus")], null=True
            ),
        ),
        migrations.AddField(
            model_name="historicalorganization",
            name="default_payment_provider",
            field=models.CharField(
                blank=True,
                choices=[("stripe", "Stripe"), ("braintree", "Braintree")],
                max_length=40,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="historicalorganization",
            name="tax_provider",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "taxjar"), (2, "lotus")], default=2
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="default_payment_provider",
            field=models.CharField(
                blank=True,
                choices=[("stripe", "Stripe"), ("braintree", "Braintree")],
                max_length=40,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="tax_provider",
            field=models.PositiveSmallIntegerField(
                choices=[(1, "taxjar"), (2, "lotus")], default=2
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="payment_provider",
            field=models.CharField(
                blank=True,
                choices=[("stripe", "Stripe"), ("braintree", "Braintree")],
                max_length=40,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="externalplanlink",
            name="source",
            field=models.CharField(
                choices=[("stripe", "Stripe"), ("braintree", "Braintree")],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="historicalcustomer",
            name="payment_provider",
            field=models.CharField(
                blank=True,
                choices=[("stripe", "Stripe"), ("braintree", "Braintree")],
                max_length=40,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalinvoice",
            name="external_payment_obj_type",
            field=models.CharField(
                blank=True,
                choices=[("stripe", "Stripe"), ("braintree", "Braintree")],
                max_length=40,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalorganizationsetting",
            name="setting_group",
            field=models.CharField(
                blank=True,
                choices=[
                    ("stripe", "Stripe"),
                    ("braintree", "Braintree"),
                    ("billing", "Billing"),
                ],
                max_length=64,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="historicalorganizationsetting",
            name="setting_name",
            field=models.CharField(
                choices=[
                    (
                        "generate_customer_after_creating_in_lotus",
                        "Generate in Stripe after Lotus",
                    ),
                    (
                        "gen_cust_in_braintree_after_lotus",
                        "Generate in Braintree after Lotus",
                    ),
                    ("subscription_filter_keys", "Subscription Filter Keys"),
                    ("payment_grace_period", "Payment Grace Period"),
                ],
                max_length=64,
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="external_payment_obj_type",
            field=models.CharField(
                blank=True,
                choices=[("stripe", "Stripe"), ("braintree", "Braintree")],
                max_length=40,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="organizationsetting",
            name="setting_group",
            field=models.CharField(
                blank=True,
                choices=[
                    ("stripe", "Stripe"),
                    ("braintree", "Braintree"),
                    ("billing", "Billing"),
                ],
                max_length=64,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="organizationsetting",
            name="setting_name",
            field=models.CharField(
                choices=[
                    (
                        "generate_customer_after_creating_in_lotus",
                        "Generate in Stripe after Lotus",
                    ),
                    (
                        "gen_cust_in_braintree_after_lotus",
                        "Generate in Braintree after Lotus",
                    ),
                    ("subscription_filter_keys", "Subscription Filter Keys"),
                    ("payment_grace_period", "Payment Grace Period"),
                ],
                max_length=64,
            ),
        ),
        migrations.CreateModel(
            name="StripeOrganizationIntegration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_account_id", models.TextField()),
                (
                    "created",
                    models.DateTimeField(default=metering_billing.utils.utils.now_utc),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stripe_organization_links",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StripeCustomerIntegration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("stripe_customer_id", models.TextField()),
                (
                    "created",
                    models.DateTimeField(default=metering_billing.utils.utils.now_utc),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stripe_customer_links",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BraintreeOrganizationIntegration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("braintree_merchant_id", models.TextField()),
                (
                    "created",
                    models.DateTimeField(default=metering_billing.utils.utils.now_utc),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="braintree_organization_links",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BraintreeCustomerIntegration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("braintree_customer_id", models.TextField()),
                (
                    "created",
                    models.DateTimeField(default=metering_billing.utils.utils.now_utc),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="braintree_customer_links",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        help_text="City, district, suburb, town, or village",
                        max_length=50,
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("AW", "Aruba"),
                            ("AF", "Afghanistan"),
                            ("AO", "Angola"),
                            ("AI", "Anguilla"),
                            ("AX", "Åland Islands"),
                            ("AL", "Albania"),
                            ("AD", "Andorra"),
                            ("AE", "United Arab Emirates"),
                            ("AR", "Argentina"),
                            ("AM", "Armenia"),
                            ("AS", "American Samoa"),
                            ("AQ", "Antarctica"),
                            ("TF", "French Southern Territories"),
                            ("AG", "Antigua and Barbuda"),
                            ("AU", "Australia"),
                            ("AT", "Austria"),
                            ("AZ", "Azerbaijan"),
                            ("BI", "Burundi"),
                            ("BE", "Belgium"),
                            ("BJ", "Benin"),
                            ("BQ", "Bonaire, Sint Eustatius and Saba"),
                            ("BF", "Burkina Faso"),
                            ("BD", "Bangladesh"),
                            ("BG", "Bulgaria"),
                            ("BH", "Bahrain"),
                            ("BS", "Bahamas"),
                            ("BA", "Bosnia and Herzegovina"),
                            ("BL", "Saint Barthélemy"),
                            ("BY", "Belarus"),
                            ("BZ", "Belize"),
                            ("BM", "Bermuda"),
                            ("BO", "Bolivia, Plurinational State of"),
                            ("BR", "Brazil"),
                            ("BB", "Barbados"),
                            ("BN", "Brunei Darussalam"),
                            ("BT", "Bhutan"),
                            ("BV", "Bouvet Island"),
                            ("BW", "Botswana"),
                            ("CF", "Central African Republic"),
                            ("CA", "Canada"),
                            ("CC", "Cocos (Keeling) Islands"),
                            ("CH", "Switzerland"),
                            ("CL", "Chile"),
                            ("CN", "China"),
                            ("CI", "Côte d'Ivoire"),
                            ("CM", "Cameroon"),
                            ("CD", "Congo, The Democratic Republic of the"),
                            ("CG", "Congo"),
                            ("CK", "Cook Islands"),
                            ("CO", "Colombia"),
                            ("KM", "Comoros"),
                            ("CV", "Cabo Verde"),
                            ("CR", "Costa Rica"),
                            ("CU", "Cuba"),
                            ("CW", "Curaçao"),
                            ("CX", "Christmas Island"),
                            ("KY", "Cayman Islands"),
                            ("CY", "Cyprus"),
                            ("CZ", "Czechia"),
                            ("DE", "Germany"),
                            ("DJ", "Djibouti"),
                            ("DM", "Dominica"),
                            ("DK", "Denmark"),
                            ("DO", "Dominican Republic"),
                            ("DZ", "Algeria"),
                            ("EC", "Ecuador"),
                            ("EG", "Egypt"),
                            ("ER", "Eritrea"),
                            ("EH", "Western Sahara"),
                            ("ES", "Spain"),
                            ("EE", "Estonia"),
                            ("ET", "Ethiopia"),
                            ("FI", "Finland"),
                            ("FJ", "Fiji"),
                            ("FK", "Falkland Islands (Malvinas)"),
                            ("FR", "France"),
                            ("FO", "Faroe Islands"),
                            ("FM", "Micronesia, Federated States of"),
                            ("GA", "Gabon"),
                            ("GB", "United Kingdom"),
                            ("GE", "Georgia"),
                            ("GG", "Guernsey"),
                            ("GH", "Ghana"),
                            ("GI", "Gibraltar"),
                            ("GN", "Guinea"),
                            ("GP", "Guadeloupe"),
                            ("GM", "Gambia"),
                            ("GW", "Guinea-Bissau"),
                            ("GQ", "Equatorial Guinea"),
                            ("GR", "Greece"),
                            ("GD", "Grenada"),
                            ("GL", "Greenland"),
                            ("GT", "Guatemala"),
                            ("GF", "French Guiana"),
                            ("GU", "Guam"),
                            ("GY", "Guyana"),
                            ("HK", "Hong Kong"),
                            ("HM", "Heard Island and McDonald Islands"),
                            ("HN", "Honduras"),
                            ("HR", "Croatia"),
                            ("HT", "Haiti"),
                            ("HU", "Hungary"),
                            ("ID", "Indonesia"),
                            ("IM", "Isle of Man"),
                            ("IN", "India"),
                            ("IO", "British Indian Ocean Territory"),
                            ("IE", "Ireland"),
                            ("IR", "Iran, Islamic Republic of"),
                            ("IQ", "Iraq"),
                            ("IS", "Iceland"),
                            ("IL", "Israel"),
                            ("IT", "Italy"),
                            ("JM", "Jamaica"),
                            ("JE", "Jersey"),
                            ("JO", "Jordan"),
                            ("JP", "Japan"),
                            ("KZ", "Kazakhstan"),
                            ("KE", "Kenya"),
                            ("KG", "Kyrgyzstan"),
                            ("KH", "Cambodia"),
                            ("KI", "Kiribati"),
                            ("KN", "Saint Kitts and Nevis"),
                            ("KR", "Korea, Republic of"),
                            ("KW", "Kuwait"),
                            ("LA", "Lao People's Democratic Republic"),
                            ("LB", "Lebanon"),
                            ("LR", "Liberia"),
                            ("LY", "Libya"),
                            ("LC", "Saint Lucia"),
                            ("LI", "Liechtenstein"),
                            ("LK", "Sri Lanka"),
                            ("LS", "Lesotho"),
                            ("LT", "Lithuania"),
                            ("LU", "Luxembourg"),
                            ("LV", "Latvia"),
                            ("MO", "Macao"),
                            ("MF", "Saint Martin (French part)"),
                            ("MA", "Morocco"),
                            ("MC", "Monaco"),
                            ("MD", "Moldova, Republic of"),
                            ("MG", "Madagascar"),
                            ("MV", "Maldives"),
                            ("MX", "Mexico"),
                            ("MH", "Marshall Islands"),
                            ("MK", "North Macedonia"),
                            ("ML", "Mali"),
                            ("MT", "Malta"),
                            ("MM", "Myanmar"),
                            ("ME", "Montenegro"),
                            ("MN", "Mongolia"),
                            ("MP", "Northern Mariana Islands"),
                            ("MZ", "Mozambique"),
                            ("MR", "Mauritania"),
                            ("MS", "Montserrat"),
                            ("MQ", "Martinique"),
                            ("MU", "Mauritius"),
                            ("MW", "Malawi"),
                            ("MY", "Malaysia"),
                            ("YT", "Mayotte"),
                            ("NA", "Namibia"),
                            ("NC", "New Caledonia"),
                            ("NE", "Niger"),
                            ("NF", "Norfolk Island"),
                            ("NG", "Nigeria"),
                            ("NI", "Nicaragua"),
                            ("NU", "Niue"),
                            ("NL", "Netherlands"),
                            ("NO", "Norway"),
                            ("NP", "Nepal"),
                            ("NR", "Nauru"),
                            ("NZ", "New Zealand"),
                            ("OM", "Oman"),
                            ("PK", "Pakistan"),
                            ("PA", "Panama"),
                            ("PN", "Pitcairn"),
                            ("PE", "Peru"),
                            ("PH", "Philippines"),
                            ("PW", "Palau"),
                            ("PG", "Papua New Guinea"),
                            ("PL", "Poland"),
                            ("PR", "Puerto Rico"),
                            ("KP", "Korea, Democratic People's Republic of"),
                            ("PT", "Portugal"),
                            ("PY", "Paraguay"),
                            ("PS", "Palestine, State of"),
                            ("PF", "French Polynesia"),
                            ("QA", "Qatar"),
                            ("RE", "Réunion"),
                            ("RO", "Romania"),
                            ("RU", "Russian Federation"),
                            ("RW", "Rwanda"),
                            ("SA", "Saudi Arabia"),
                            ("SD", "Sudan"),
                            ("SN", "Senegal"),
                            ("SG", "Singapore"),
                            ("GS", "South Georgia and the South Sandwich Islands"),
                            ("SH", "Saint Helena, Ascension and Tristan da Cunha"),
                            ("SJ", "Svalbard and Jan Mayen"),
                            ("SB", "Solomon Islands"),
                            ("SL", "Sierra Leone"),
                            ("SV", "El Salvador"),
                            ("SM", "San Marino"),
                            ("SO", "Somalia"),
                            ("PM", "Saint Pierre and Miquelon"),
                            ("RS", "Serbia"),
                            ("SS", "South Sudan"),
                            ("ST", "Sao Tome and Principe"),
                            ("SR", "Suriname"),
                            ("SK", "Slovakia"),
                            ("SI", "Slovenia"),
                            ("SE", "Sweden"),
                            ("SZ", "Eswatini"),
                            ("SX", "Sint Maarten (Dutch part)"),
                            ("SC", "Seychelles"),
                            ("SY", "Syrian Arab Republic"),
                            ("TC", "Turks and Caicos Islands"),
                            ("TD", "Chad"),
                            ("TG", "Togo"),
                            ("TH", "Thailand"),
                            ("TJ", "Tajikistan"),
                            ("TK", "Tokelau"),
                            ("TM", "Turkmenistan"),
                            ("TL", "Timor-Leste"),
                            ("TO", "Tonga"),
                            ("TT", "Trinidad and Tobago"),
                            ("TN", "Tunisia"),
                            ("TR", "Turkey"),
                            ("TV", "Tuvalu"),
                            ("TW", "Taiwan, Province of China"),
                            ("TZ", "Tanzania, United Republic of"),
                            ("UG", "Uganda"),
                            ("UA", "Ukraine"),
                            ("UM", "United States Minor Outlying Islands"),
                            ("UY", "Uruguay"),
                            ("US", "United States"),
                            ("UZ", "Uzbekistan"),
                            ("VA", "Holy See (Vatican City State)"),
                            ("VC", "Saint Vincent and the Grenadines"),
                            ("VE", "Venezuela, Bolivarian Republic of"),
                            ("VG", "Virgin Islands, British"),
                            ("VI", "Virgin Islands, U.S."),
                            ("VN", "Viet Nam"),
                            ("VU", "Vanuatu"),
                            ("WF", "Wallis and Futuna"),
                            ("WS", "Samoa"),
                            ("YE", "Yemen"),
                            ("ZA", "South Africa"),
                            ("ZM", "Zambia"),
                            ("ZW", "Zimbabwe"),
                        ],
                        help_text="Two-letter country code (ISO 3166-1 alpha-2)",
                        max_length=2,
                        validators=[
                            django.core.validators.MinLengthValidator(2),
                            django.core.validators.MaxLengthValidator(2),
                        ],
                    ),
                ),
                (
                    "line1",
                    models.TextField(
                        help_text="Address line 1 (e.g., street, PO Box, or company name)",
                        max_length=100,
                    ),
                ),
                (
                    "line2",
                    models.TextField(
                        help_text="Address line 2 (e.g., apartment, suite, unit, or building)",
                        null=True,
                    ),
                ),
                (
                    "postal_code",
                    models.CharField(help_text="ZIP or postal code", max_length=20),
                ),
                (
                    "state",
                    models.CharField(
                        help_text="State, county, province, or region",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="addresses",
                        to="metering_billing.organization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="billing_address",
            field=models.ForeignKey(
                blank=True,
                help_text="The billing address for the customer",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="billing_customers",
                to="metering_billing.address",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="braintree_integration",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="customers",
                to="metering_billing.braintreecustomerintegration",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="shipping_address",
            field=models.ForeignKey(
                blank=True,
                help_text="The shipping address for the customer",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="shipping_customers",
                to="metering_billing.address",
            ),
        ),
        migrations.AddField(
            model_name="customer",
            name="stripe_integration",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="customers",
                to="metering_billing.stripecustomerintegration",
            ),
        ),
        migrations.AddField(
            model_name="historicalcustomer",
            name="billing_address",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="The billing address for the customer",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.address",
            ),
        ),
        migrations.AddField(
            model_name="historicalcustomer",
            name="braintree_integration",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.braintreecustomerintegration",
            ),
        ),
        migrations.AddField(
            model_name="historicalcustomer",
            name="shipping_address",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="The shipping address for the customer",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.address",
            ),
        ),
        migrations.AddField(
            model_name="historicalcustomer",
            name="stripe_integration",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.stripecustomerintegration",
            ),
        ),
        migrations.AddField(
            model_name="historicalorganization",
            name="address",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                help_text="The primary origin address for the organization",
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.address",
            ),
        ),
        migrations.AddField(
            model_name="historicalorganization",
            name="braintree_integration",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.braintreeorganizationintegration",
            ),
        ),
        migrations.AddField(
            model_name="historicalorganization",
            name="stripe_integration",
            field=models.ForeignKey(
                blank=True,
                db_constraint=False,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="+",
                to="metering_billing.stripeorganizationintegration",
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="address",
            field=models.ForeignKey(
                blank=True,
                help_text="The primary origin address for the organization",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="metering_billing.address",
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="braintree_integration",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="organizations",
                to="metering_billing.braintreeorganizationintegration",
            ),
        ),
        migrations.AddField(
            model_name="organization",
            name="stripe_integration",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="organizations",
                to="metering_billing.stripeorganizationintegration",
            ),
        ),
        migrations.AddConstraint(
            model_name="stripeorganizationintegration",
            constraint=models.UniqueConstraint(
                fields=("organization", "stripe_account_id"),
                name="unique_stripe_account_id",
            ),
        ),
        migrations.AddConstraint(
            model_name="stripecustomerintegration",
            constraint=models.UniqueConstraint(
                fields=("organization", "stripe_customer_id"),
                name="unique_stripe_customer_id",
            ),
        ),
        migrations.AddConstraint(
            model_name="braintreeorganizationintegration",
            constraint=models.UniqueConstraint(
                fields=("organization", "braintree_merchant_id"),
                name="unique_braintree_merchant_id",
            ),
        ),
        migrations.AddConstraint(
            model_name="braintreecustomerintegration",
            constraint=models.UniqueConstraint(
                fields=("organization", "braintree_customer_id"),
                name="unique_braintree_customer_id",
            ),
        ),
    ]
