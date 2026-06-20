class Solution:
    def simplifyPath(self, path: str) -> str:
        directories = []
        current_dir = ""

        for i in range(len(path)):
            if path[i] != '/':
                current_dir += path[i]

            if path[i] == '/' or i == len(path) - 1:
                if current_dir == '.':
                    current_dir = ''
                    continue
                if current_dir == ".." and directories:
                    directories.pop()
                else:
                    if current_dir and current_dir != "..":
                        directories.append(current_dir)
                current_dir = ''

        res = '/'
        joined_dirs = '/'.join(directories)
        return res + joined_dirs

# Loop through string
# Use a stack to store file directories
# Hold current directory name which will be added onto until a slash is found
# When slash is found, add directory name to stack and reset variable holding name
# If name slash is found and variable is empty, don't add anything to stack
# Another variable can be used to keep count of periods seen until we hit a slash
# When we hit a slash, reset to 0.
# Otherwise, keep counting periods.
# If we hit slash and periods more == 2, pop from stack
# If period just 1, do nothing and reset.
