informations = []
suppliers = []
activities = []

# Information Flow
print("Enter the information flow (Type 'end' to Stop) : ")

i = 0
while(True):
  print("Enter the component "+str(i + 1)+" detail")
  information = input()
  if information == "end":
    break
  informations.append(information)
  i = i + 1
print(informations)

# Supplier
print("Enter the Supplier Details (Type 'end' to Stop) : ")

i = 0
while(True):
  print("Enter the supplier "+str(i + 1)+" details")
  supplier_name = input("Name : ")
  if supplier_name == "end":
    break
  supplier_interval = input("Intervel : ")
  supplier = {"Name":supplier_name, "Intervel":supplier_interval}
  suppliers.append(supplier)
  i = i + 1
print(suppliers)

# Process Flow
print("Enter the activity flow (Type 'end' to Stop) : ")

i = 0
while(True):
  act_code = input("Enter activity "+ str(i + 1) +" code (end_act to stop)")
  if(act_code == "end_act"):
    break
  flag = True
  activity_status = True
  sub_activities = []
  while(True):
    status = int(input("Enter 1 if the process is a waiting process, 10 to exit else 0"))
    if status == 10:
      break
    if status == 1:
      activity_status = False
    else:
      activity_status = True
    sub_act_name = input("Enter the name of activity : ")
    lot_size = input("Enter the lot size : ")
    cycle_time = input("Cycle Time : ")
    if activity_status and flag:
      flag = False
      equipments = []
      while(True):
        equipment_name = input("Equipment Name (end_eqp to break): ")
        if(equipment_name == "end_eqp"):
          break
        equipment_cost = input("Capital Cost : ")
        equipment_maintenance_cost = input("Maintenence Cost : ")
        equipment_total_usage = input("Total Usage per Year : ")
        equipment = {
          "name": equipment_name,
          "cost": equipment_cost,
          "maintenence": equipment_maintenance_cost,
          "usage": equipment_total_usage
        }
        equipments.append(equipment)
      supervisor_count = input("Number of supervisors : ")
      operator_count = input("Number of operators : ")
      operator_cost = input("Operator cost : ")
      operator_time = input("Operation time : ")
      material_cost = input("Material cost : ")
      sub_activity = {
        "type": "activity",
        "name": sub_act_name,
        "lot_size": lot_size,
        "equipments": equipments,
        "supervisor_count": supervisor_count,
        "operator_count": operator_count,
        "operator_cost": operator_cost,
        "operator_time": operator_time,
        "material_cost": material_cost,
        "cycle_time": cycle_time
      }
      sub_activities.append(sub_activity)
    else:
      waiting_time = input("Waiting time before process")
      sub_activity = {
        "type": "waiting",
        "name": sub_act_name,
        "lot_size": lot_size,
        "cycle_time": cycle_time,
        "waiting_time": waiting_time
      }
      sub_activities.append(sub_activity)
  rejection = input("Percentage rejection")
  activity = {
    "code": act_code,
    "sub_activities": sub_activities,
    "rejection": rejection
  }
  activities.append(activity)
print(activities)