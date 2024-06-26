import unittest
from unittest.mock import patch

from exercises.algorithmic.basic import *
from exercises.algorithmic.input_output import *
from exercises.algorithmic.function import *
from exercises.algorithmic.string import *
from exercises.algorithmic.data_structure import *
from exercises.algorithmic.list import *
from exercises.algorithmic.dictionary import *
from exercises.algorithmic.tuple import *
from exercises.algorithmic.set import *
from exercises.algorithmic.oop import *
from exercises.algorithmic.datetime import *
from exercises.algorithmic.json_ex import *


class TestingBasic(unittest.TestCase):
    def test_make_calculation(self):
        self.assertEqual(make_calculation(20, 30), "The result is 600.")
        self.assertEqual(make_calculation(40, 30), "The result is 70.")

    @patch("builtins.input", return_value="pynative")
    def test_print_char(self, mock_input):
        expected_output = "p\nn\nt\nv\n"
        self.assertEqual(print_char(), expected_output)

    def test_remove_chars(self):
        self.assertEqual(remove_chars("pynative", 4), "tive")
        self.assertEqual(remove_chars("pynative", 2), "native")

    def test_check_first_last_number(self):
        self.assertEqual(check_first_last_number([10, 20, 30, 40, 10]), True)
        self.assertEqual(check_first_last_number([75, 65, 35, 75, 30]), False)

    def test_display_5_fold(self):
        self.assertEqual(display_5_fold([10, 20, 33, 46, 55]), [10, 20, 55])

    def test_is_palindrom(self):
        self.assertEqual(is_palindrom("545"), True)
        self.assertEqual(is_palindrom("145"), False)

    def test_new_list(self):
        self.assertEqual(
            new_list([10, 20, 25, 30, 35], [40, 45, 60, 75, 90]), [25, 35, 40, 60, 90]
        )

    def test_exponent(self):
        self.assertEqual(exponent(2, 2), 4)
        self.assertEqual(exponent(5, 2), 25)


class TestingInputAndOutput(unittest.TestCase):
    @patch("builtins.input", side_effect=["2", "3"])
    def test_make_user_calculation(self, mock_input):
        self.assertEqual(make_user_calculation(), 6)

    @patch("builtins.input", side_effect=["8", "3"])
    def test_make_user_calculation(self, mock_input):
        self.assertEqual(make_user_calculation(), 24)

    def test_display_string(self):
        self.assertEqual(
            display_string("Hello", "world,", "Loïc"), "Hello**world,**Loïc"
        )

    def test_display_octal(self):
        self.assertEqual(display_octal(650), 1212)
        self.assertEqual(display_octal(550), 1046)
        self.assertEqual(display_octal(1550), 3016)

    def test_display_float(self):
        self.assertEqual(display_float(3.141516), 3.14)
        self.assertEqual(display_float(458.541315), 458.54)

    @patch("builtins.input", return_value=("1.2 1.5 1.6"))
    def test_display_list(self, mock_input):
        self.assertEqual(display_list(), [1.2, 1.5, 1.6])


class TestingFunction(unittest.TestCase):
    def test_presentation(self):
        self.assertEqual(
            presentation("Loïc", 31), "My name is Loïc and I'm 31 years old."
        )

    def test_func1(self):
        self.assertEqual(func1("20", "20"), "20\n20\n")
        self.assertEqual(func1("20", "30", "40"), "20\n30\n40\n")

    def test_calculation(self):
        self.assertEqual(calculation(40, 10), [50, 30])

    def test_show_employee(self):
        self.assertEqual(show_employee("Loïc", 10500), "Name: Loïc Salary: 10500")
        self.assertEqual(show_employee("John"), "Name: John Salary: 9000")

    def test_outer_function(self):
        self.assertEqual(outer_function(5, 10), 20)

    def test_recursiv(self):
        self.assertEqual(recursiv(10), 55)

    def test_display_student(self):
        self.assertEqual(
            show_student("Loïc", 31), "My name is Loïc and I'm 31 years old."
        )

    def test_even_list(self):
        self.assertEqual(even_list(), [4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28])

    def test_largest_item(self):
        self.assertEqual(largest_item([4, 6, 8, 24, 12, 2]), 24)


class TestingString(unittest.TestCase):
    def test_blend_string(self):
        self.assertEqual(blend_string("hello", "world"), "heworldllo")
        self.assertEqual(blend_string("Ault", "Kelly"), "AuKellylt")

    def test_blend_string_v2(self):
        self.assertEqual(blend_string_v2("Hello", "World"), "HWlrod")
        self.assertEqual(blend_string_v2("America", "Japan"), "AJrpan")

    def test_first_lowercase(self):
        self.assertEqual(first_lowercase("PyNaTive"), "yaivePNT")

    def test_count_sum_avg(self):
        self.assertEqual(
            count_sum_avg("PYnative29@#8496"), "Sum: 38 Average: 6.333333333333333"
        )

    def test_remove_empty_s(self):
        self.assertEqual(
            remove_empty_s(["Emma", "Jon", "", "Kelly", None, "Eric", ""]),
            ["Emma", "Jon", "Kelly", "Eric"],
        )

    def test_remove_special_chars(self):
        self.assertEqual(
            remove_special_chars("/*Jon is @developer & musician"),
            "Jon is developer  musician",
        )

    def test_remove_all_letters(self):
        self.assertEqual(remove_all_letters("I am 25 years and 10 months old"), "2510")

    def test_remove_special_chars(self):
        self.assertEqual(
            replace_special_chars("/*Jon is @developer & musician!!"),
            "##Jon is #developer # musician##",
        )


class TestingDataStructure(unittest.TestCase):
    def test_create_new_list(self):
        self.assertEqual(
            create_new_list([3, 6, 9, 12, 15, 18, 21], [4, 8, 12, 16, 20, 24, 28]),
            [6, 12, 18, 4, 12, 20, 28],
        )

    def test_remove_add_into_list(self):
        self.assertEqual(
            remove_add_into_list([34, 54, 67, 89, 11, 43, 94]),
            [34, 54, 11, 67, 89, 43, 94, 11],
        )

    def test_count_occurs(self):
        self.assertEqual(
            count_occurs([11, 45, 8, 11, 23, 45, 23, 45, 89]),
            {11: 2, 45: 3, 8: 1, 23: 2, 89: 1},
        )

    def test_zip_set(self):
        self.assertEqual(
            zip_set([2, 3, 4, 5, 6, 7, 8], [4, 9, 16, 25, 36, 49, 64]),
            {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)},
        )

    def test_exist_dict_list(self):
        self.assertEqual(
            exist_dict_list(
                [47, 64, 69, 37, 76, 83, 95, 97],
                {"Jhon": 47, "Emma": 69, "Kelly": 76, "Jason": 97},
            ),
            [47, 69, 76, 97],
        )

    def test_find_min_max(self):
        self.assertEqual(
            find_min_max([87, 45, 41, 65, 94, 41, 99, 94]), "Min: 41 Max: 99"
        )


class TestingList(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual(
            reverse_list([100, 200, 300, 400, 500]), [500, 400, 300, 200, 100]
        )

    def test_concat_list(self):
        self.assertEqual(
            concat_list(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"]),
            ["My", "name", "is", "Kelly"],
        )

    def test_square_list(self):
        self.assertEqual(square_list([1, 2, 3, 4, 5, 6, 7]), [1, 4, 9, 16, 25, 36, 49])

    def test_concat_list_v2(self):
        self.assertEqual(
            concat_list_v2(["Hello ", "take "], ["Dear", "Sir"]),
            ["Hello Dear", "Hello Sir", "take Dear", "take Sir"],
        )

    def test_iterate_simultaneously(self):
        self.assertEqual(
            iterate_simultaneously([10, 20, 30, 40], [100, 200, 300, 400]),
            [(10, 400), (20, 300), (30, 200), (40, 100)],
        )

    def test_add_specific_item(self):
        self.assertEqual(
            add_specific_item([10, 20, [300, 400, [5000, 6000], 500], 30, 40]),
            [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40],
        )

    def test_nested_list(self):
        self.assertEqual(
            extend_nested_list(
                ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"],
                ["h", "i", "j"],
            ),
            [
                "a",
                "b",
                ["c", ["d", "e", ["f", "g", "h", "i", "j"], "k"], "l"],
                "m",
                "n",
            ],
        )


class TestingDictionary(unittest.TestCase):
    def test_transform_list_into_dict(self):
        self.assertEqual(
            transform_list_into_dict(["Ten", "Twenty", "Thirty"], [10, 20, 30]),
            {"Ten": 10, "Twenty": 20, "Thirty": 30},
        )

    def test_merge_dict(self):
        self.assertEqual(
            merge_dict(
                {"Ten": 10, "Twenty": 20, "Thirty": 30},
                {"Thirty": 30, "Fourty": 40, "Fifty": 50},
            ),
            {"Ten": 10, "Twenty": 20, "Thirty": 30, "Fourty": 40, "Fifty": 50},
        )

    def test_nested_dict(self):
        sampleDict = {
            "class": {
                "student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}
            }
        }
        self.assertEqual(nested_dict(sampleDict), 80)

    def test_initialize_dist(self):
        self.assertEqual(
            initialize_dict(
                ["Kelly", "Emma"], {"designation": "Developer", "salary": 8000}
            ),
            {
                "Kelly": {"designation": "Developer", "salary": 8000},
                "Emma": {"designation": "Developer", "salary": 8000},
            },
        )

    def test_extract_keys(self):
        sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
        keys = ["name", "salary"]

        self.assertEqual(
            extract_keys(sampleDict, keys), {"name": "Kelly", "salary": 8000}
        )

    def test_delete_keys(self):
        sampleDict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
        keys = ["name", "salary"]

        self.assertEqual(delete_keys(sampleDict, keys), {"city": "New york", "age": 25})

    def test_check_values(self):
        self.assertEqual(
            check_values({"a": 100, "b": 200, "c": 300}, 200),
            "La valeur '200' est bien présente",
        )
        self.assertEqual(check_values({"a": 100, "b": 200, "c": 300}, 20), None)

    def test_min_key(self):
        sample_dict = {"Physics": 82, "Math": 65, "history": 75}

        self.assertEqual(min_key(sample_dict), "Math")

    def test_update_nested_dictionary(self):
        sample_dict = {
            "emp1": {"name": "Jhon", "salary": 7500},
            "emp2": {"name": "Emma", "salary": 8000},
            "emp3": {"name": "Brad", "salary": 500},
        }

        new_dict = {
            "emp1": {"name": "Jhon", "salary": 7500},
            "emp2": {"name": "Emma", "salary": 8000},
            "emp3": {"name": "Brad", "salary": 8500},
        }

        self.assertEqual(update_nested_dictionary(sample_dict), new_dict)


class TestingTuple(unittest.TestCase):
    def test_reverse_tuple(self):
        self.assertEqual(reverse_tuple((10, 20, 30, 40, 50)), (50, 40, 30, 20, 10))

    def test_access_value(self):
        self.assertEqual(access_value(("Orange", [10, 20, 30], (5, 15, 25))), 20)

    def test_swap_tuple(self):
        self.assertEqual(swap_tuple((11, 22), (99, 88)), ((99, 88), (11, 22)))

    def test_copy_elem(self):
        self.assertEqual(copy_elem((11, 22, 33, 44, 55, 66)), (44, 55))

    def test_update_tuple(self):
        self.assertEqual(update_tuple((11, [22, 33], 44, 55)), (11, [222, 33], 44, 55))

    def test_sort_tuple(self):
        self.assertEqual(
            sort_tuple((("a", 23), ("b", 37), ("c", 11), ("d", 29))),
            (("c", 11), ("a", 23), ("d", 29), ("b", 37)),
        )


class TestingSet(unittest.TestCase):
    def test_add_list_to_set(self):
        self.assertEqual(
            add_list_to_set(["Blue", "Green", "Red"], {"Yellow", "Orange", "Black"}),
            {"Green", "Yellow", "Black", "Orange", "Red", "Blue"},
        )

    def test_intersection_set(self):
        self.assertEqual(
            intersection_set({10, 20, 30, 40, 50}, {30, 40, 50, 60, 70}), {40, 50, 30}
        )

    def test_union_set(self):
        self.assertEqual(
            union_set({10, 20, 30, 40, 50}, {30, 40, 50, 60, 70}),
            {70, 40, 10, 50, 20, 60, 30},
        )

    def test_difference_update(self):
        self.assertEqual(difference_update({10, 20, 30}, {20, 40, 50}), {10, 30})

    def test_remove_items(self):
        self.assertEqual(remove_items({10, 20, 30, 40, 50}), {40, 50})

    def test_symmetric_difference(self):
        self.assertEqual(
            symmetric_diff({10, 20, 30, 40, 50}, {30, 40, 50, 60, 70}), {20, 70, 10, 60}
        )

    def test_disjoint(self):
        self.assertEqual(disjoint({10, 20, 30, 40, 50}, {60, 70, 80, 90, 10}), {10})

    def test_symmetric_diff_update(self):
        self.assertEqual(
            symmetric_diff_update({10, 20, 30, 40, 50}, {30, 40, 50, 60, 70}),
            {70, 10, 20, 60},
        )

    def test_intersection_update(self):
        self.assertEqual(
            intersection_update({10, 20, 30, 40, 50}, {30, 40, 50, 60, 70}),
            {40, 50, 30},
        )


class TestingOOP(unittest.TestCase):
    def test_vehicle(self):
        vehicle_class = Vehicle("car", 80, 24, 20)
        self.assertEqual(vehicle_class.max_speed, 80)
        self.assertEqual(vehicle_class.mileage, 24)

    def test_bus(self):
        bus_class = Bus("bus", 180, 12, 50)
        self.assertEqual(
            bus_class.display_attributes(),
            "Color: White Vehicle Name: bus Speed: 180 Mileage: 12",
        )
        self.assertEqual(
            bus_class.seating_capacity(),
            "The seating capacity of a bus is 50 passengers",
        )
        self.assertEqual(bus_class.fare(), "Total Bus fare is: 5500.0")

    def test_car(self):
        car_class = Car("Audi Q5", 240, 18, 5)
        self.assertEqual(
            car_class.display_attributes(),
            "Color: White Vehicle Name: Audi Q5 Speed: 240 Mileage: 18",
        )

    def test_type_object(self):
        self.assertEqual(type_object(Car("Audi Q5", 240, 18, 5)), Car)

    def test_is_instance(self):
        bus_class = Bus("bus", 180, 12, 50)
        self.assertEqual(is_instance(bus_class, Vehicle), True)


class TestingDatetime(unittest.TestCase):
    def test_transform_into_datetime(self):
        self.assertEqual(
            transform_into_datetime("Feb 25 2020 4:20PM"), "2020-02-25 16:20:00"
        )

    def test_time_delta(self):
        self.assertEqual(time_delta(2020, 2, 25), "2020-02-18")

    def test_format_date(self):
        self.assertEqual(format_date(2020, 2, 25), "Tuesday 25 February 2020")

    def test_find_day_name(self):
        self.assertEqual(find_day_name(2020, 7, 26), "Sunday")


class TestingJSON(unittest.TestCase):
    def test_extract_key(self):
        sampleJson = """{"key1": "value1", "key2": "value2"}"""
        self.assertEqual(extract_key(sampleJson), "value2")

    def test_nested_key(self):
        sampleJson = {
            "company": {
                "employee": {"name": "emma", "payble": {"salary": 7000, "bonus": 800}}
            }
        }

        self.assertEqual(nested_key(sampleJson), 7000)

    def test_convert_json_into_object(self):
        class Vehicle:
            def __init__(self, name, engine, price):
                self.name = name
                self.engine = engine
                self.price = price

        sampleJson = '{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}'
        self.assertEqual(
            convert_json_into_object(Vehicle, sampleJson),
            ("Toyota Rav4", "2.5L", 32000),
        )

    def test_is_valid_json(self):
        sampleJson = """{ "company":{ "employee":{ "name":"emma", "payble":{ "salary":7000 "bonus":800} } } }"""
        self.assertEqual(is_valid_json(sampleJson), False)


if __name__ == "__main__":
    unittest.main()
