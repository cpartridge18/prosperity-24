from datamodel import OrderDepth, UserId, TradingState, Order
from typing import List
import string
import logging

class Trader:

    def run(self, state: TradingState):
        #takes in a trading state, outputs list of orders to send
        #logging.print(test)
        tradeOrders = {}
        for product in state.order_depths:
            match product:
                case "AMETHYSTS":
                    tradeOrders[product] = self.amethystsTrader(state.order_depths[product], state.position.get(product, 0))

        traderData = "Knowledge for the future" #delivered as TradeingState.traderdata
        return tradeOrders, 1, traderData
    
    def amethystsTrader(self, orderDepth, currentPosition):
        #logging.print(currentPosition)
        positionLimit = 20
        buyLimit = positionLimit - currentPosition
        sellLimit = positionLimit + currentPosition
        neutralPrice = 10000
        orders: List[Order] = []

        active_buy_orders = list(orderDepth.buy_orders.items())
        active_buy_orders.sort(key = lambda x: x[0], reverse = True)
        for price, quantity in active_buy_orders:
            if price > neutralPrice + 1:
                if quantity < sellLimit:
                    orders.append(Order("AMETHYSTS", price, -quantity))
                    sellLimit -= quantity
                else:
                    orders.append(Order("AMETHYSTS", price, -sellLimit))
                    break
            else:
                break

        active_sell_orders = list(orderDepth.sell_orders.items())
        active_sell_orders.sort(key = lambda x: x[0])
        for price, quantity in active_sell_orders:
            if price < neutralPrice - 1:
                if abs(quantity) <= buyLimit:
                    orders.append(Order("AMETHYSTS", price, -quantity))
                    buyLimit += quantity
                else:
                    orders.append(Order("AMETHYSTS", price, buyLimit))
                    break
            else:
                break
        return orders

    def starFruitTrader(self):
        #look at observations and analyze maybe
        pass