from django.db import migrations

def add_sample_questions(apps, schema_editor):
    Question = apps.get_model('quiz', 'Question')

    questions = [
        {
            'question_text': 'What is the capital of France?',
            'option_a': 'Berlin',
            'option_b': 'Madrid',
            'option_c': 'Paris',
            'option_d': 'Rome',
            'correct_option': 'c',
        },
        {
            'question_text': 'What is 2 + 2?',
            'option_a': '3',
            'option_b': '4',
            'option_c': '5',
            'option_d': '6',
            'correct_option': 'b',
        },
        {
            'question_text': 'What is the color of the sky?',
            'option_a': 'Blue',
            'option_b': 'Red',
            'option_c': 'Green',
            'option_d': 'Yellow',
            'correct_option': 'a',
        },
        {
            'question_text': 'What is the largest planet in our solar system?',
            'option_a': 'Earth',
            'option_b': 'Jupiter',
            'option_c': 'Saturn',
            'option_d': 'Mars',
            'correct_option': 'b',
        },
        {
            'question_text': 'Who wrote the play "Romeo and Juliet"?',
            'option_a': 'Shakespeare',
            'option_b': 'Dickens',
            'option_c': 'Hemingway',
            'option_d': 'Austen',
            'correct_option': 'a',
        },
        {
            'question_text': 'What is the square root of 16?',
            'option_a': '2',
            'option_b': '4',
            'option_c': '8',
            'option_d': '6',
            'correct_option': 'b',
        },
        {
            'question_text': 'Who painted the Mona Lisa?',
            'option_a': 'Vincent van Gogh',
            'option_b': 'Leonardo da Vinci',
            'option_c': 'Pablo Picasso',
            'option_d': 'Claude Monet',
            'correct_option': 'b',
        },
        {
            'question_text': 'What is the largest ocean on Earth?',
            'option_a': 'Atlantic Ocean',
            'option_b': 'Indian Ocean',
            'option_c': 'Arctic Ocean',
            'option_d': 'Pacific Ocean',
            'correct_option': 'd',
        },
        {
            'question_text': 'Which country is known as the Land of the Rising Sun?',
            'option_a': 'China',
            'option_b': 'Japan',
            'option_c': 'Korea',
            'option_d': 'India',
            'correct_option': 'b',
        },
        {
            'question_text': 'What is the boiling point of water in Celsius?',
            'option_a': '90°C',
            'option_b': '100°C',
            'option_c': '120°C',
            'option_d': '110°C',
            'correct_option': 'b',
        },
        {
            'question_text': 'What is the main ingredient in guacamole?',
            'option_a': 'Tomato',
            'option_b': 'Avocado',
            'option_c': 'Onion',
            'option_d': 'Lime',
            'correct_option': 'b',
        },
        {
            'question_text': 'Which gas do plants use for photosynthesis?',
            'option_a': 'Oxygen',
            'option_b': 'Nitrogen',
            'option_c': 'Carbon Dioxide',
            'option_d': 'Helium',
            'correct_option': 'c',
        },
        {
            'question_text': 'Which continent is known as the "Dark Continent"?',
            'option_a': 'Asia',
            'option_b': 'Africa',
            'option_c': 'Australia',
            'option_d': 'Antarctica',
            'correct_option': 'b',
        },
        {
            'question_text': 'Which instrument is used to measure temperature?',
            'option_a': 'Thermometer',
            'option_b': 'Barometer',
            'option_c': 'Altimeter',
            'option_d': 'Speedometer',
            'correct_option': 'a',
        },
        {
            'question_text': 'What is the capital of Japan?',
            'option_a': 'Seoul',
            'option_b': 'Tokyo',
            'option_c': 'Beijing',
            'option_d': 'Hanoi',
            'correct_option': 'b',
        },
        {
            'question_text': 'What is the fastest land animal?',
            'option_a': 'Lion',
            'option_b': 'Cheetah',
            'option_c': 'Elephant',
            'option_d': 'Horse',
            'correct_option': 'b',
        },
        {
            'question_text': 'Which planet is known as the Red Planet?',
            'option_a': 'Mars',
            'option_b': 'Venus',
            'option_c': 'Jupiter',
            'option_d': 'Saturn',
            'correct_option': 'a',
        },
        {
            'question_text': 'What is the smallest prime number?',
            'option_a': '0',
            'option_b': '1',
            'option_c': '2',
            'option_d': '3',
            'correct_option': 'c',
        },
        {
            'question_text': 'Which element is represented by the symbol O?',
            'option_a': 'Oxygen',
            'option_b': 'Osmium',
            'option_c': 'Oganesson',
            'option_d': 'Ozone',
            'correct_option': 'a',
        },
        {
            'question_text': 'What is the capital of the United Kingdom?',
            'option_a': 'Paris',
            'option_b': 'London',
            'option_c': 'Berlin',
            'option_d': 'Madrid',
            'correct_option': 'b',
        },
        {
            'question_text': 'Which organ in the human body pumps blood?',
            'option_a': 'Brain',
            'option_b': 'Heart',
            'option_c': 'Liver',
            'option_d': 'Lung',
            'correct_option': 'b',
        }
    ]

    for question in questions:
        Question.objects.create(**question)

class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_questions),
    ]
