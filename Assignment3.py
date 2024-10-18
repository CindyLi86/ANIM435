import maya.cmds as cmds
import argparse

# Command-line argument parser setup
def setup_argparse():
    parser = argparse.ArgumentParser(description='Extrude vertices and split edges in Maya.')
    
    subparsers = parser.add_subparsers(dest='command', help='Sub-command to run')

    # Sub-parser for extruding vertices
    extrude_parser = subparsers.add_parser('extrude', help='Extrude vertices with divisions and length')
    extrude_parser.add_argument('--divisions', type=int, default=1, help='Number of divisions for extrude (1-10)')
    extrude_parser.add_argument('--length', type=float, default=1.0, help='Extrusion length (0.1-5.0)')

    # Sub-parser for splitting edges
    split_parser = subparsers.add_parser('split', help='Split edges with divisions')
    split_parser.add_argument('--divisions', type=int, default=1, help='Number of divisions for edge split (1-10)')

    return parser.parse_args()

# Function for extruding vertices
def extrude_vertices(divisions, length):
    selected_verts = cmds.ls(selection=True, flatten=True)
    if not selected_verts:
        print("No vertices selected for extrusion!")
        return

    for vert in selected_verts:
        cmds.polyExtrudeVertex(vert, divisions=divisions, length=length)

    print(f"Extruded vertices with {divisions} divisions and length {length}")

# Function for splitting edges
def split_edges(divisions):
    selected_edges = cmds.ls(selection=True, flatten=True)
    if not selected_edges:
        print("No edges selected for splitting!")
        return

    for edge in selected_edges:
        cmds.polySplitEdge(edge, divisions=divisions)

    print(f"Split edges with {divisions} divisions")

# Main function to handle the command-line logic
def main():
    args = setup_argparse()

    if args.command == 'extrude':
        extrude_vertices(args.divisions, args.length)
    elif args.command == 'split':
        split_edges(args.divisions)
    else:
        print("Please provide a valid command: 'extrude' or 'split'.")

# If running as a script within Maya, invoke the main function
if __name__ == "__main__":
    main()
