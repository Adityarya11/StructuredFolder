import os
import streamlit as st
from streamlit_tree_select import tree_select

st.set_page_config(layout="wide", page_title="Folder Structure Tool")

st.title("Structured Folder")


def build_tree_and_get_paths(path):
    """
    Recursively builds a tree structure and collects all file/folder paths.
    
    Returns:
        tuple: (list of tree nodes, list of all paths)
    """
    nodes = []
    all_keys = []
    
    try:
        with os.scandir(path) as it:
            # Sort: folders first, then files alphabetically
            entries = sorted(list(it), key=lambda e: (not e.is_dir(), e.name.lower()))
            
            for entry in entries:
                # Skip hidden files and folders
                if entry.name.startswith('.'):
                    continue
                
                all_keys.append(entry.path)
                
                node = {
                    "label": entry.name,
                    "value": entry.path,
                }
                
                if entry.is_dir():
                    children, child_keys = build_tree_and_get_paths(entry.path)
                    node["children"] = children
                    all_keys.extend(child_keys)
                
                nodes.append(node)
                
    except PermissionError:
        pass
        
    return nodes, all_keys


def get_all_children_paths(tree_data, parent_path):
    """
    Recursively collects all child paths under a given parent path.
    
    Args:
        tree_data: List of tree nodes
        parent_path: The parent folder path to search for
        
    Returns:
        list: All descendant paths including the parent
    """
    children_paths = []
    
    for node in tree_data:
        if node["value"] == parent_path:
            # Found the parent, collect all its descendants
            children_paths.append(node["value"])
            if "children" in node:
                children_paths.extend(_collect_all_descendants(node["children"]))
            return children_paths
        elif "children" in node:
            # Recursively search in children
            result = get_all_children_paths(node["children"], parent_path)
            if result:
                return result
    
    return children_paths


def _collect_all_descendants(nodes):
    """
    Helper function to collect all paths from a list of nodes recursively.
    
    Args:
        nodes: List of tree nodes
        
    Returns:
        list: All paths in the tree
    """
    paths = []
    for node in nodes:
        paths.append(node["value"])
        if "children" in node:
            paths.extend(_collect_all_descendants(node["children"]))
    return paths


def is_directory_path(path):
    """Check if a path represents a directory."""
    return os.path.isdir(path)


# Initialize with current working directory
default_path = os.getcwd()
folder_path = st.text_input("Enter Local Folder Path:", value=default_path)

if folder_path and os.path.isdir(folder_path):
    
    # Detect folder change and reset session state
    if "current_folder" not in st.session_state or st.session_state["current_folder"] != folder_path:
        st.session_state["current_folder"] = folder_path
        
        # Build tree structure for the new folder
        tree_data, all_paths = build_tree_and_get_paths(folder_path)
        
        # Initialize session state with all items selected and expanded
        st.session_state["tree_data"] = tree_data
        st.session_state["checked_files"] = all_paths
        st.session_state["expanded_folders"] = all_paths

    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("1. Select/Deselect Files")
        
        # Select All / Deselect All buttons
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            if st.button("Select All", use_container_width=True):
                tree_data, all_paths = build_tree_and_get_paths(folder_path)
                st.session_state["checked_files"] = all_paths
                st.rerun()
        
        with btn_col2:
            if st.button("Deselect All", use_container_width=True):
                st.session_state["checked_files"] = []
                st.rerun()
        
        # Render the tree selection widget
        return_val = tree_select(
            st.session_state["tree_data"],
            checked=st.session_state["checked_files"],
            expanded=st.session_state["expanded_folders"],
            key=f"tree_widget_{folder_path}",
        )
        
        # Detect changes in checked items
        new_checked = set(return_val["checked"])
        old_checked = set(st.session_state["checked_files"])
        
        # Find newly checked items (difference between new and old)
        newly_checked = new_checked - old_checked
        
        # For each newly checked item, if it's a folder, include all its children
        additional_paths = set()
        for path in newly_checked:
            if is_directory_path(path):
                # Get all children of this folder
                children = get_all_children_paths(st.session_state["tree_data"], path)
                additional_paths.update(children)
        
        # Combine: original checked items + newly added children
        final_checked = list(new_checked | additional_paths)
        
        # Update session state if changed
        if set(final_checked) != old_checked:
            st.session_state["checked_files"] = final_checked
            st.rerun()

    # Generate the output tree structure
    selected_paths = set(st.session_state["checked_files"])

    with col2:
        st.subheader("2. Result")
        
        if not selected_paths:
            st.warning("No files selected.")
        else:
            output_lines = []
            root_depth = folder_path.count(os.sep)
            sorted_paths = sorted(list(selected_paths))
            
            # Add root folder name
            output_lines.append(os.path.basename(folder_path) + "/")
            
            for path in sorted_paths:
                # Skip the root folder itself
                if path == folder_path:
                    continue
                
                # Calculate indentation based on depth
                rel_depth = path.count(os.sep) - root_depth
                indent = "│   " * (rel_depth - 1) + "├── "
                
                name = os.path.basename(path)
                
                # Add trailing slash for directories
                if is_directory_path(path):
                    name += "/"
                
                output_lines.append(f"{indent}{name}")

            final_tree = "\n".join(output_lines)
            st.code(final_tree, language="text")

else:
    st.error("Path not found or invalid directory.")