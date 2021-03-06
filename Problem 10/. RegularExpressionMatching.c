bool isMatch(char* s, char* p) {
if(s == NULL || p == NULL) 
    return false;
if(*p==0) 
    return *s == 0;
if(*(p+1) == '*')
    do{
        if(isMatch(s,p+2)) 
            return true;
    }while(*s && (*p == *(s++) || *p == '.'));
else if(*p == *s || (*p == '.' && *s!=0))
    return isMatch(++s,++p);
return false;
}
