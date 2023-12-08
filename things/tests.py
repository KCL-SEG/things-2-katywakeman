from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .forms import ThingForm

class ThingFormTestCase(TestCase):
    # Create your tests here.
    def setUp(self):
        self.form_input = {
            "name" : "Thing1",
            "description" : "This is my thing description",
            "quantity" : 5
        }

    #test 
    def test_valid_input(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())
    
    def test_quantity_must_be_under_50(self):
        self.form_input["quantity"] = 51
        form = ThingForm(data=self.form_input)
        self.assertFalse(form.is_valid())