import os
import maya.cmds as cmds

# Access the 'SHOT' environment variable
shot = os.getenv('SHOT')

if not shot:
    print("Environment variable 'SHOT' is not set.")
else:
    # Use the environment variable to name new geometry
    geo = f"{shot}_cube"
    if not cmds.objExists(geo):
        # Create a cube and name it based on the shot name
        cube = cmds.polyCube(name=geo)[0]
        print(f"Created geometry: {geo}")
        
        # Create a custom attribute on the geometry
        custom_attr = "customAttribute"
        if not cmds.attributeQuery(custom_attr, node=geo, exists=True):
            cmds.addAttr(geo, longName=custom_attr, attributeType="float", defaultValue=0.0)
            cmds.setAttr(f"{geo}.{custom_attr}", keyable=True)
            print(f"Added custom attribute '{custom_attr}' to {geo}")
        
        # Save the scene with a filename based on the environment variable
        save_filename = f"{shot}_geometry_scene.mb"
        cmds.file(rename=save_filename)
        cmds.file(save=True, type="mayaBinary")
        print(f"Scene saved as: {save_filename}")
    else:
        print(f"Geometry '{geo}' already exists in the scene.")
