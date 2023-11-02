import json

def load_data(file_path, json_file_path):  
    data_dict = {}  
    with open(file_path, 'r') as file:
        for line in file:
            print(line)
            # Split each line into a list of items using a specific delimiter (e.g., comma)
            line_items = line.strip().split(', ')
           
            
            key = line_items[0]
            values = ', '.join(line_items[1:])
            print(key)
            # Store the data in the dictionary
            data_dict[key] = values
            print("values",values)
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        
   

        #print("filename ", image_filename, "object detections ", object_detections)
    return data, data_dict

detections, labels = load_data('/home/tylermckenzie/hand_object_detector/tea/mapped_labels.txt', '/home/tylermckenzie/hand_object_detector/tea/object_detections.json')


 
def generate_detections(hand_data, action_data):
    left_obj = "none"
    right_obj = "none"

    for frame in hand_data:
        image_filename = frame["image_filename"]
       
        # Check if there is a corresponding action label
        
        if image_filename in action_data: 
            action_label = action_data[image_filename]
            print(action_label)
            print(image_filename)
            left_bbox = None
            right_bbox = None
            for detection in object_detections:
                if detection["left_right"] == 0:
                    
                    left_bbox = detection["box"]
                else:
                    right_bbox = detection["box"]
                    

            left_obj, right_obj = generate_obj_label(action_label, left_obj, right_obj, left_bbox, right_bbox)
            print(left_obj, right_obj)

        object_detections = frame["object_detections"]
        
        # if len(object_detections) == 2:
        #     if (object_detections[0]["box"][0] == object_detections[1]["box"][0] and
        #         object_detections[0]["box"][1] == object_detections[1]["box"][1] and
        #         object_detections[0]["box"][2] == object_detections[1]["box"][2] and
        #         object_detections[0]["box"][3] == object_detections[1]["box"][3]):
        #         if left_obj == "none":
        #             object_detections[0]["object_label"] = right_obj 
        #             print("yas")
        #         elif right_obj == "none":
        #             object_detections[1]["object_label"] = left_obj
        #             print("yas")
        #     else:
        #          object_detections[0]["object_label"] = left_obj 
        #          object_detections[1]["object_label"] = right_obj 
        # # # Update object labels for each detection in the frame
        # else:
        for detection in object_detections:
            if detection["left_right"] == 0:
                
                detection["object_label"] = left_obj
            else:
                detection["object_label"] = right_obj


    print("Saved to json file")
    output_json_file = 'tea_det.json'
    with open(output_json_file, 'w') as json_file:
        json.dump(hand_data, json_file, ensure_ascii=False, indent=4)
    print("Saved to json file", output_json_file)


def generate_obj_label(action_label, left_obj, right_obj, left_bbox, right_bbox):
    action_label = action_label.split(",")
    
    print("Pick up" in action_label[0])
    #if something is picked up, switch to the next obj
    if "Pick up" in action_label[0] or "Open" in action_label[0] or "Take" in action_label[0]:
        if  right_bbox != None and right_obj == "none":
            right_obj = action_label[-1]
        elif  left_bbox != None and left_obj == "none":
            left_obj = action_label[-1]
        else:
            print("Something was put down but not annotated as such!")

    elif "Put down" in action_label[0] or "Close" in action_label[0] or "Place" in action_label[0]:
        print("i'm being put down")
        if right_obj == action_label[-1]:
            right_obj = "none"
        elif left_obj == action_label[-1]:
            left_obj = "none"
        else:
            print("Something was picked up and not annotated as such!")
    elif "Switch" in action_label[0]:
        old_right = right_obj
        right_obj = left_obj
        left_obj = old_right 

            
    print(left_obj, right_obj)
    return left_obj, right_obj



generate_detections(detections, labels)

        
