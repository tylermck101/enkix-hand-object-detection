# Define a custom mapping dictionary for action-noun pairs to object detection labels
action_noun_to_labels = {
    "measuring cup": "measuring:cup",
    "Measure water": "measuring:cup",
    "Pour water": "kettle",
    "Pick up tea bag": "tea:bag",
    "Open tea bag": "tea:bag",
    "Place tea bag": "tea:bag, cup",
    "Check temperature": "thermometer, kettle",
    "Put down thermometer": "thermometer",
    "Pour water": "kettle",
    "Pick up tea bag": "tea:bag",
    "Place tea bag": "tea:bag",
    "Stir": "spoon",
    "tortilla bag": "tortilla:bag",
    "Pick up Nutella jar": "nutella:jar",
    "Open Nutella jar": "nutella:jar, lid",
    "Scoop Nutella": "nutella:jar, knife",
    "Put down Nutella jar": "nutella:jar",
    "Spread Nutella": "knife, tortilla",
    "Pick up paper towel": "paper:towel",
    "Clean knife": "knife, paper:towel",
    "Cut banana": "banana,knife",
    "banana slice": "banana:slice",
    "Place tortilla wedge": "tortilla:wedge",
    "Cut tortilla": "tortilla, knife",
    "Scoop oats": "oats:container, spoon",
    "Take oats": "Take oats:container",
    "Open oats": "Open oats:container",
    "Close oats": "Close oats:container, lid",
    "Place oats": "Place oats:container",
    "raisin bag": "raisin:bag",
    "nut butter jar": "nut:butter:jar",
    "Scoop nut butter": "nut:butter:jar, knife",
    "Spread nut butter": "knife",
    "jelly jar": "jelly:jar",
    "Scoop jelly": "jelly:jar, knife",
    "Clean knife": "knife, paper:towel",
    "Cut rolled tortilla": "tortilla, knife",
    "paper filter": "paper:filter",
    "kitchen scale": "scale",
    "coffee grinder": "coffee:grinder",
    "coffee beans": "coffee:beans",
    "Scoop coffee grounds": "spoon, coffee:grinder"

    
}

def map_action_noun_to_labels(file_path, action_noun_to_labels, output_file_path):
    context = "measuring cup"
    with open(file_path, 'r') as file, open(output_file_path, 'w') as output_file:
        lines = file.readlines()
        for line in lines:
            parts = line.split(',')
            action_noun = parts[5].strip()
            noun = parts[7].strip()
            timestamp = parts[0]  
            if action_noun == 'pour water':
                if context == 'measuring cup':
                    detection_label = 'measuring:cup'
                    context == 'kettle'
                elif context == 'kettle':
                    detection_label == 'Take,kettle'
            elif action_noun in action_noun_to_labels:
                #   print('measuring cup' in action_noun_to_labels)
                  detection_label = action_noun_to_labels[action_noun]
                #   print(detection_label)
            elif noun in action_noun_to_labels:
                 detection_label = action_noun_to_labels[noun]
                 print(detection_label)
            else:
                # print(action_noun)
                detection_label = action_noun.split()[-1]
                print(detection_label)
            if "Take" in parts[5] or "Place" in parts[5] or "Put down" in parts[5] or "Pick up" in parts[5] or "Open" in parts[5] or "Close" in parts[5]:
                detection_label = parts[6] + "," + detection_label
            print(parts[3] == 1, parts[3])
            if(int(parts[3]) == 1):
                output_file.write(f"{timestamp}, {detection_label}\n")


file_path = '/home/tylermckenzie/hand_object_detector/9-19-oatmeal/actions.txt'
output_file_path = '/home/tylermckenzie/hand_object_detector/9-19-oatmeal/mapped_labels.txt'
map_action_noun_to_labels(file_path, action_noun_to_labels, output_file_path)

