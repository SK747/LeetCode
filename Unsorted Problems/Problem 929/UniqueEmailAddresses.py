class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
            
        unique_emails = set()
        
        for e in emails:
            local=  e.split('@')[0].split('+')[0].replace('.','') ## Can do this all in one line
            domain = e.split('@')[1]
            valid_email = local+'@'+domain

            unique_emails.add(valid_email)

        return len(unique_emails)