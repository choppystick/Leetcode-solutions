# R solution for 1233. Remove Sub-Folders from the Filesystem

removeSubfolders <- function(folder) {
  folder <- sort(folder)
  result <- list(folder[1])
  
  for (i in 2:length(folder)) {
    current <- folder[i]
    last_parent <- tail(result, 1)[[1]]
    
    # Check if `current` is a subfolder of `last_parent`
    if (!(startsWith(current, last_parent) && substr(current, nchar(last_parent) + 1, nchar(last_parent) + 1) == "/")) {
      result <- append(result, current)
    }
  }
  
  return(unlist(result))
}