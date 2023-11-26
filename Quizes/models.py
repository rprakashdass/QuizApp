from django.db import models
import random
DIFFICULT_CHOICES = (
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)

class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    no_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Quiz Duration in Minutes")
    score_to_pass = models.IntegerField(help_text="Score in %")
    difficulty = models.CharField(max_length=20, choices=DIFFICULT_CHOICES)

    def __str__(self):
        return f"{self.name} - {self.topic}"
    
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.no_of_questions]
    
    class Meta:
        verbose_name_plural = 'Quizes'