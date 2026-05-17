# INSERT INTO [table] () VALUES ()
def insertQueryGenerator():
  # Declarations
  query = "INSERT INTO "
  attributes = int
  numberOfinserts = int
  table = str
  arguments = []
  inserts = []

  # Quantity inputs
  try:
    attributes = int(input("Enter the number of attributes: "))
    numberOfinserts = int(input("Enter the number of inserts: "))
  except:
    print("Please enter a number (1-n)!")
    insertQueryGenerator()

  table = str(input("Enter the name of the table: "))

  # Insert structure inputs
  # Attributes
  for i in range(attributes):
    arguments.append(input(f"Enter the {i+1}º element of the table: "))

  prefix = str(input("Does any attribute have a prefix? (y/N): "))
  
  lenOfCount = 1
  prefixPlace = -1
  if (prefix.lower() == "y"):
    print("Wich position has a prefix:")
    for i in range(attributes):
      print(f"{i+1}. [{arguments[i]}]")
    prefixPlace = int(input("Enter a number: "))
    prefixPlace -= 1

    prefix = str(input("What is the prefix: "))
    lenOfCount = int(input("Enter the size of the sufix (number of digits): "))
    if lenOfCount < 1: lenOfCount = 1

  # Values structure
  count = 10 ** (lenOfCount - 1)

  for i in range(numberOfinserts):
    values = []
    for j in range(attributes):
      if prefixPlace == j:
        values.append("'" + prefix + str(count))
      else:
        values.append("'" + str(count))

    # inside the "()" in values
    places = "', ".join(values) + "'"

    # Values composition
    inserts.append(f"({places})")
    
    count += 1


  # String generation
  query += table
  query += " (" + ", ".join(arguments) + ") " + "VALUES\n"
  query += ",\n".join(inserts) + ";"

  return print(query)
    

insertQueryGenerator()
input("Press enter to exit . . .")