""" Food object, stores value and calories of the item """
class Food(object):
    def __init__(self, name, value, calories):
        self.name = name
        self.value = value
        self.calories = calories
    def getValue(self):
        return self.value
    def getCalories(self):
        return self.calories
    def getRatio(self):
        return self.value / self.calories
    def __str__(self):
        return self.name + ' (' + str(self.value) + ', ' + str(self.calories) + ')'

""" buildMenu, makes a list of items of Food """
def buildMenu(names, values, calories):
    menu = []
    for i in range(len(names)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

""" greedy, solves the knapsack problem using the given key """
def greedy(items, maxCalories, key):
    sortedItems = sorted(items, key = key, reverse = True)  # Always descending

    result = []
    totalValue, totalCalories = 0.0, 0.0
    for item in sortedItems:
        if (item.getCalories() + totalCalories) <= maxCalories:
            result.append(item)
            totalValue += item.getValue()
            totalCalories += item.getCalories()
    return (result, totalValue)

""" Runs the greedy and shows the results """
def testGreedy(items, maxCalories, key):    
    result, totalValue = greedy(items, maxCalories, key)
    print('Total value is', totalValue)
    for item in result:
        print('\t', item)

""" testGreedys, runs the algorthim using different keys """
def testGreedys(items, maxCalories):
    # key = value
    print('Use greedy by value to allocate', maxCalories, 'calories')
    testGreedy(items, maxCalories, Food.getValue)

    # key = calories
    print('\nUse greedy by cost to allocate', maxCalories, 'calories')
    testGreedy(items, maxCalories, lambda x: 1/Food.getCalories(x))

    # key = value / calories
    print('\nUse greedy by density to allocate', maxCalories, 'calories')
    testGreedy(items, maxCalories, Food.getRatio)

""" Initialization and run """
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10, 20]
calories = [123, 154, 258, 354, 365, 150, 95, 195, 200]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)
