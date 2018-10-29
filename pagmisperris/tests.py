from django.test import TestCase
from .models import Post
from django.utils import timezone

class PostTestCase( TestCase ):
  def test_postPublish1( self ):
	#Arrange
	expected=2
	result=2
	#act
	result=2
	#assert
	self.assertAreEqual(expected,result)

  def test_postPublish2( self ):
	#Arrange
	expected=4
	result=1
	#act
	result=5
	#assert
	self.assertAreEqual(expected,result)

  def test_postPublish3( TestCase ):
	#Arrange
	expected=5
	result=1
	#act
	result=6
	#assert
	self.assertAreEqual(expected,result)


