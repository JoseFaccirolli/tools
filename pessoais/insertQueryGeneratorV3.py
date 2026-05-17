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

  op = str(input("Does any attribute have a prefix? (y/N): "))
  
  prefix = []
  lenOfCount = 1
  prefixPlace = -1
  if (op.lower() == "y"):
    for i in range(attributes):
      print("(If there is no prefix just press enter!)")
      prefix.append(input(f"Enter the prefix of [{arguments[i]}]: "))

  lenOfCount = int(input("Enter the minimun counter size (the number of digits of the suffix): "))
  if lenOfCount < 1: lenOfCount = 1

  # Values structure
  count = 10 ** (lenOfCount - 1)

  for i in range(numberOfinserts):
    values = []
    for j in range(attributes):
      if op.lower() == "y":
        values.append("'" + prefix[j] + str(count))
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