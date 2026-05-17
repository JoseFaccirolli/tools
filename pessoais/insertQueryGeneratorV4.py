# INSERT INTO [table] () VALUES ()
def insertQueryGenerator():
  # Declarations
  query = "INSERT INTO "
  numberOfAttributes = int
  numberOfinserts = int
  table = str
  attributes = []
  inserts = []

  # Quantity inputs
  try:
    numberOfAttributes = int(input("Enter the number of attributes: "))
    numberOfinserts = int(input("Enter the number of inserts: "))
  except:
    print("Please enter a number (1-n)!")
    insertQueryGenerator()

  table = str(input("Enter the name of the table: "))

  # Insert structure inputs
  # Attributes
  for i in range(numberOfAttributes):
    attributes.append(input(f"Enter the {i+1}º element of the table: "))

  op = str(input("Does any attribute have a prefix or have a fixed value? (y/N): "))
  
  prefix = []
  isFixed = []
  fixedValue = []
  lenOfCount = 1
  if (op.lower() == "y"):
    # Prefix
    for i in range(numberOfAttributes):
      print("(If there is no prefix (or is a fixed value) just press enter!)")
      prefix.append(input(f"Enter the prefix of [{attributes[i]}]: "))

    # Fixed value
    for i in range(numberOfAttributes):
      print("(Type 'y' or 'n' if this attribute have a fixed value")
      isFixed.append(input( 60 * "-" + "\n" + f"The attribute [{attributes[i]}] has a fixed value? (y/N): ").lower())
      if isFixed[i] == "y":
        fixedValue.append(input(f"Enter the fixed value of [{attributes[i]}]: "))


  lenOfCount = int(input("Enter the minimun counter size (the number of digits of the suffix): "))
  if lenOfCount < 1: lenOfCount = 1

  # Values structure
  count = 10 ** (lenOfCount - 1)
  fix_count = 0
  for i in range(numberOfinserts):
    values = []
    fix_count = 0
    for j in range(numberOfAttributes):
      if op.lower() == "y" and isFixed[j] != "y":
        values.append("'" + prefix[j] + str(count))
      elif len(isFixed) > 0 and isFixed[j] == "y":
        values.append(fixedValue[fix_count])
        fix_count += 1
      else:
        values.append("'" + str(count))

    # inside the "()" in values
    places = "', ".join(values) + "'"

    # Values composition
    inserts.append(f"({places})")
    
    count += 1


  # String generation
  query += table
  query += " (" + ", ".join(attributes) + ") " + "VALUES\n"
  query += ",\n".join(inserts) + ";"

  return print(query)
    

insertQueryGenerator()
input("Press enter to exit . . .")