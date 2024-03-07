from django.db import models


class SpecificationManager(models.Manager):
    def get_specs_keys(self, product_id):
        specs_keys = []
        specs = super().get_queryset().filter(product__id=product_id)
        for i in specs:
            for j in i.specification:
                if j not in specs_keys:
                    specs_keys.append(j)
        print(specs_keys)
        return None

    def get_specs_key_value(self, product_id):
        specs_keys = {}
        specs = super().get_queryset().filter(product__id=product_id)

        for spec in specs:
            for key, value in spec.specification.items():
                if key in specs_keys:
                    if value not in specs_keys[key]:
                        specs_keys[key].append(value)
                else:
                    specs_keys[key] = [value]

        specs_list = [{key: values} for key, values in specs_keys.items()]
        return specs_list
