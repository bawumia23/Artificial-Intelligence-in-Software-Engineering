#ifdef DEBUG
    #define LOG_MSG(fmt, ...) \
        fprintf(stderr, "[%s:%d] " fmt "\n", __FILE__, __LINE__, ##__VA_ARGS__)
#else
    #define LOG_MSG(fmt, ...) ((void)0)
#endif
