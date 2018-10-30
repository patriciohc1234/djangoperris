from django.test import TestCase
from .models import Post
from django.utils import timezone

class TestCase1( TestCase ):

    def test_Post1( self ):
      #Arrange
      expected = 1
      result = 0
      #Act
      Post.objects.create( author = "patricio", title="Sample Title" , text="Test")
      #Assert
      self.assertEqual(expected,result)

class TestCase1( TestCase ):

   def test_Post2( self ):
     #Arrange
     expected = 1
     result = 0
     #Act
     Post.objects.filter(published_date__lte=timezone.now()
     #Assert
     self.assertEqual(expected,result)



