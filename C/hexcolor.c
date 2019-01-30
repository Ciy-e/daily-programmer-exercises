
char hex_chars[] = "0123456789ABCDEF";

int left_hex_char(int i) 
{
    return (i & 0xF0) >> 4;
}

int right_hex_char(int i) 
{
    return (i & 0x0F);
}

char get_left_char(int i)
{
    return hex_chars[left_hex_char(i)];
}

char get_right_char(int i)
{
    return hex_chars[right_hex_char(i)];
}

void rgb_to_hex(int r, int g, int b, char *buff)
{
    int index = 0;
    buff[index++] = '#';
    buff[index++] = left_hex_char(r);
    buff[index++] = right_hex_char(r);
    buff[index++] = left_hex_char(g);
    buff[index++] = right_hex_char(g);
    buff[index++] = left_hex_char(b);
    buff[index++] = right_hex_char(b);
    buff[index++] = '\0'; 

}