from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()

        for email in emails:
            names = email.split("@")
            local = names[0]
            domain = names[1]

            local = local.replace(".", "")
            if '+' in local:
                plus_idx = local.index('+')
                local = local[0: plus_idx]
            
            new_email = f"{local}@{domain}"
            unique_emails.add(new_email)
        

        print(list(unique_emails))
        return len(unique_emails)
