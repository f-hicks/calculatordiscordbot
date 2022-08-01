import discord
import ast
import operator as op

operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul,
             ast.Div: op.truediv, ast.Pow: op.pow, ast.BitXor: op.xor,
             ast.USub: op.neg}

intents = discord.Intents.all()
client = discord.Client(intents=intents)

def eval_expr(expr):
    try:
        expr = expr.replace('x','*')
        expr = expr.replace('X','*')
        expr = expr.replace('k','e3')
        expr = expr.replace('K','e3')
        expr = expr.replace('m','e6')
        expr = expr.replace('M','e6')
        expr = expr.replace('b','e9')
        expr = expr.replace('B','e9')
        return eval_(ast.parse(expr, mode='eval').body)
    except:
        return
def eval_(node):
    if isinstance(node, ast.Num): # <number>
        return node.n
    elif isinstance(node, ast.BinOp): # <left> <operator> <right>
        return operators[type(node.op)](eval_(node.left), eval_(node.right))
    elif isinstance(node, ast.UnaryOp): # <operator> <operand> e.g., -1
        return operators[type(node.op)](eval_(node.operand))
    else:
        raise TypeError(node)



@client.event
async def on_ready():
    print("The bot is ready!")
@client.event
async def on_message(message):
    if message.author == client.user:
       return
    
    answer = eval_expr(message.content)
    if answer != None: await message.channel.send(f'{message.content} = {answer}')
client.run('MTAwMjI5ODA4OTU3NjYxNjEwNw.GQixCq.1PIqpK92SEdVWo7xt0MI1wfvYMOFQjlr9YBuk8')
