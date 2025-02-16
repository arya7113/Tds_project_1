# Function summaries

# A2
# format_file_with_prettier(file_path:str, prettier_version='3.4.2')

# A3
# count_wednesdays_in_dates(input_file_path=r"/data/dates.txt", output_file_path=r"/data/dates-wednesdays.txt")


tools = [
    # A1
    {
        "type": "function",
        "function": {
            "name": "run_datagen_script",
            "description": "Install uv if required and run the run datagen script at the given URL with the given email as the only argument",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_email": {
                        "type": "string",
                        "description": "User email to be passed as the argument to the datagen script",
                    },
                    "script_url": {
                        "type": "string",
                        "description": "URL from which the datagen script will be downloaded",
                    },
                },
                "required": ["user_email", "script_url"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A2
    {
        "type": "function",
        "function": {
            "name": "format_file_with_prettier",
            "description": "Format a markdown file using Prettier and update it in place.",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "The path to the markdown file that needs to be formatted.",
                    },
                    "prettier_version": {
                        "type": "string",
                        "description": "The version of Prettier to use for formatting (default is 3.4.2).",
                        # "default": "3.4.2",
                    },
                },
                "required": ["file_path", "prettier_version"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A3
    {
        "type": "function",
        "function": {
            "name": "count_given_weekday_in_dates",
            "description": "Count the number of Wednesdays in a list of dates and write the count to a file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "day_of_week": {
                        "type": "string",
                        "description": "Day of week to be counted, e.g. wednesday",
                    },
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing a list of dates, one per line.",
                        # "default": "/data/dates.txt",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the number of Wednesdays will be written.",
                        # "default": "/data/dates-wednesdays.txt",
                    },
                },
                "required": ["day_of_week", "input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A4
    {
        "type": "function",
        "function": {
            "name": "sort_contacts_file",
            "description": "Sort the contacts in the json input file by last_name then by first_name and write to given output file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing the contacts to be sorted",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the sorted contacts will be written.",
                        # "default": "/data/dates-wednesdays.txt",
                    },
                },
                "required": ["input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A5
    {
        "type": "function",
        "function": {
            "name": "write_most_recent_log_first_lines",
            "description": "Write the first line of n most recent log files in input folder to output path.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_folder": {
                        "type": "string",
                        "description": "Path to the input folder containing the log file to be processed",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted contents of the log file  will be written.",
                        # "default": "/data/dates-wednesdays.txt",
                    },
                    "num_files": {
                        "type": "integer",
                        "description": "Number of most recent log files from which the content will be processed",
                        # "default": "/data/dates-wednesdays.txt",
                    },
                },
                "required": ["input_folder", "output_file_path", "num_files"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A6
    {
        "type": "function",
        "function": {
            "name": "extract_titles_from_markdown_files",
            "description": "Recursively traverse folder and extract first H1 title from each markdown file and write to output file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_folder": {
                        "type": "string",
                        "description": "Path to the input folder containing the markdown files to be processed",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted contents of the markdown files will be written.",
                    },
                },
                "required": ["input_folder", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A7
    {
        "type": "function",
        "function": {
            "name": "extract_sender_email",
            "description": "Extract sender's email from the given email message by passing it to the LLM model and write it to the given output file",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing email message",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted sender's email ID will be written",
                    },
                },
                "required": ["input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A7
    {
        "type": "function",
        "function": {
            "name": "extract_sender_email",
            "description": "Extract sender's email from the given email message by passing it to the LLM model and write it to the given output file",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing email message",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted sender's email ID will be written",
                    },
                },
                "required": ["input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
# A7
    {
        "type": "function",
        "function": {
            "name": "extract_sender_email",
            "description": "Extract sender's email from the given email message by passing it to the LLM model and write it to the given output file",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing email message",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted sender's email ID will be written",
                    },
                },
                "required": ["input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A8
    {
        "type": "function",
        "function": {
            "name": "extract_numbers_from_image",
            "description": "Extract any type of numbers from the given image located at input path and writes those numbers at the provided output path",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing image from which the numbers need to be extracted",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the extracted numbers will be written",
                    },
                },
                "required": ["input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A9
    {
        "type": "function",
        "function": {
            "name": "get_similar_comments",
            "description": "Use text embeddings to find out the pair of most similar comments in the given input file and write those to the given output file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing the comments",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the pair of most similar comments will be written",
                    },
                },
                "required": ["input_file_path", "output_file_path"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
    # A10
    {
        "type": "function",
        "function": {
            "name": "calculate_ticket_sales",
            "description": "Find out total sales for the given ticket type in the given input file which is sqlite database with table tickets and columns type, units and price. Write the number in the given output file",
            "parameters": {
                "type": "object",
                "properties": {
                    "input_file_path": {
                        "type": "string",
                        "description": "Path to the input file containing the database with ticket sales data",
                    },
                    "output_file_path": {
                        "type": "string",
                        "description": "Path to the output file where the value of ticket sales will be written",
                    },
                    "ticket_type": {
                        "type": "string",
                        "description": "Type of ticket for which the sales need to be calculated",
                    },
                },
                "required": ["input_file_path", "output_file_path", "ticket_type"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    },
]

business_tools = [
    {
        "type": "function",
        "function": {
            "name": "fetch_api_data",
            "description": "Fetch data from an API and save it to a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "API endpoint URL"},
                    "output_path": {"type": "string", "description": "Path to save the data"}
                },
                "required": ["url", "output_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "run_sql_query",
            "description": "Run a SQL query and save results",
            "parameters": {
                "type": "object",
                "properties": {
                    "db_path": {"type": "string", "description": "Path to the database file"},
                    "query": {"type": "string", "description": "SQL query to execute"},
                    "output_path": {"type": "string", "description": "Path to save results"}
                },
                "required": ["db_path", "query", "output_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "process_image",
            "description": "Process an image (compress or resize)",
            "parameters": {
                "type": "object",
                "properties": {
                    "image_path": {"type": "string", "description": "Path to input image"},
                    "output_path": {"type": "string", "description": "Path to save processed image"},
                    "operation": {"type": "string", "enum": ["compress", "resize"]},
                    "quality": {"type": "integer", "minimum": 1, "maximum": 100},
                    "dimensions": {"type": "object", "properties": {
                        "width": {"type": "integer"},
                        "height": {"type": "integer"}
                    }}
                },
                "required": ["image_path", "output_path", "operation"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "convert_markdown",
            "description": "Convert Markdown to HTML",
            "parameters": {
                "type": "object",
                "properties": {
                    "md_path": {"type": "string", "description": "Path to Markdown file"},
                    "html_path": {"type": "string", "description": "Path to save HTML file"}
                },
                "required": ["md_path", "html_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "filter_csv",
            "description": "Filter CSV file based on criteria",
            "parameters": {
                "type": "object",
                "properties": {
                    "csv_path": {"type": "string", "description": "Path to CSV file"},
                    "filter_criteria": {"type": "object", "description": "Filter criteria"},
                    "output_path": {"type": "string", "description": "Path to save filtered data"}
                },
                "required": ["csv_path", "filter_criteria", "output_path"]
            }
        }
    }
]

# Add business tools to existing tools list
tools.extend(business_tools)