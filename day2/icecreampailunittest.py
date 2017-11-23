class IceCreamUnitTest:

	'this class is used to tst all the happenings of icecreampail'

	def __init__(self):
		self.init = True

	def testIceCreamPail(self, tmpIceCreamPail):

		#test for each mutation methods


	def testGetPriceWithGST(tmpIceCreamPail):
		expected = 12.6
		result = tmpIceCreamPail.testGetPriceWithGST()
		print(expected == result)
