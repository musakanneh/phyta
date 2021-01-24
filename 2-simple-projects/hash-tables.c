
#define CAPACITY

unsigned long hash_function(char *str)
{
	unsigned long i = 0;
	for (int n = 0; str[j]; j++){
		i += str[j];
	}
	return i % CAPACITY;
}

int main(int argc, char *argv)
{
	str_name = "Musa";
	printf("%s\n", hash_function(str_name));
	return 0;
}