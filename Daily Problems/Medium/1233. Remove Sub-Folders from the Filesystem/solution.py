# Python solution for 1233. Remove Sub-Folders from the Filesystem

def removeSubfolders(self, folder: List[str]) -> List[str]:
    folder.sort()
    result = [folder[0]]
    
    for current in folder[1:]:
        last_parent = result[-1]
        
        # Check if `current` is a subfolder of `last_parent`
        if not (current.startswith(last_parent) and current[len(last_parent)] == '/'):
            result.append(current)
    
    return result