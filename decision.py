def decide(detected_objects):
    if not detected_objects:
        return "Path is clear"
    
    # 1. IMMEDIATE DANGER (Only if touching camera)
    for obj in detected_objects:
        if obj["dist"] == "very close":
            name = obj['label'] if obj['label'] != "Object" else "Obstacle"
            return f"Stop! {name} is dangerously close!"

    # 2. SCENE SUMMARY (If safe, describe the scene)
    main_obj = detected_objects[0]
    
    # Check for a second background object
    second_obj = None
    if len(detected_objects) > 1:
        second_obj = detected_objects[1]

    # Construct the sentence
    main_text = f"{main_obj['label']} is {main_obj['dist']} on your {main_obj['pos']}"
    
    if second_obj:
        return f"{main_text}, and {second_obj['label']} is {second_obj['dist']}."
    else:
        return f"I see a {main_text}."