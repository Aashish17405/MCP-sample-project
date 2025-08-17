from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    print(f"Adding {a} and {b}")
    """_summary_
    Add two numbers
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    print(f"Subtracting {b} from {a}")
    """
    Subtract two numbers
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    print(f"Multiplying {a} and {b}")
    """
    Multiply two numbers
    """
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    print(f"Dividing {a} by {b}")
    """
    Divide two numbers
    """
    if b == 0:
        return 0
    return a / b

# The transport="stdio" argument tells the server to use standard input/output(stdin and stdout) to receive and respond to tool function calls

if __name__ == "__main__":
    mcp.run(transport="stdio")