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

""" Search tree to sove knapsack problem """
def searchTree(food, availColories):
    if food == [] or availColories == 0:
        result = (0, ())
    elif food[0].getCalories() > availColories:
        result = searchTree(food[1:], availCallories)
    else:
        nextItem = food[0]
        # Check if we take the item
        withVal, withToTake = searchTree(food[1:], availColories - nextItem.getCalories())
        withVal += nextItem.getValue()

        # Check if we don't take the item
        withoutVal, withoutToTake = searchTree(food[1:], availColories)

        # Check the best choice
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutTake)

    return result

""" Prints the results """
def testSearchTree(foods, maxCalories):
    print('Use search tree to allocate', maxCalories, 'calories')
    val, items = searchTree(foods, maxCalories)
    print('Total value of items taken =', val)
    items = sorted(items, key = Food.getValue, reverse = True)
    for item in items:
        print('\t', item)

""" Initialization and run """
names = ['wine', 'beer', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89, 90, 95, 100, 90, 79, 50, 10, 20]
calories = [123, 154, 258, 354, 365, 150, 95, 195, 200]
foods = buildMenu(names, values, calories)
testSearchTree(foods, 1000)
