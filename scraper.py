from lxml import html
import requests

class juice:
	name = ""
	ingredients = []
	infographicURL = ""
	picURL = ""
	def __init__(self,name,ingredients,infographicURL,picURL):
		self.name = name
		self.ingredients = ingredients
		self.infographicURL = infographicURL
		self.picURL = picURL

landingPage = requests.get('https://juicerecipes.com/recipes/')
tree = html.fromstring(landingPage.text)
pagination = tree.xpath('//ul[@class="pagination pagination-lg"]/li/a/@href')
count = len(pagination);

print count
juices =[]
for i in range(1,count+1):
	page = requests.get('https://juicerecipes.com/recipes/'+'?page='+str(i))
	tree = html.fromstring(page.text)
	recipe_urls = tree.xpath('//h2[@class="panel-title"]/a/@href')

	for recipeURL in recipe_urls:
		print recipeURL

		recipe_page = requests.get("https://juicerecipes.com"+recipeURL)
		recipe_page_tree = html.fromstring(recipe_page.text)

		name = recipe_page_tree.xpath('//h2[@class="page-header"]/text()')[0]
		ingredients = recipe_page_tree.xpath('//ul[@class="green-list"]/li/text()')
		infographicURL = recipe_page_tree.xpath('//img[@class="img-rounded img-responsive"]/@data-pin-media')[0]
		picURL = "https://juicerecipes.com"+recipe_page_tree.xpath('//img[@class="img-rounded img-responsive"]/@src')[0]

		juices.append(juice(name,ingredients,infographicURL,picURL))


print len(juices)
for juice in juices:
	print juice.name
	print juice.ingredients
	print juice.infographicURL
	print juice.picURL



