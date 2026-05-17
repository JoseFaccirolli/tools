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

  # Values structure
  count = 0
  for i in range(numberOfinserts):
    values = []
    for j in range(attributes):
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