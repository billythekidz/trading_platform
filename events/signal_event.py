from events.event import Event


class SignalEvent(Event):
    def __init__(self, strategy_id, symbol, bar_datetime, datetime, signal_type, strength, stop_loss=None,
                 take_profit=None, trade_id_to_exit=None):
        """
        Initialises the SignalEvent.

        Parameters:
        strategy_id - The unique identifier for the strategy that generated the signal.
        symbol - The ticker symbol, e.g. 'EURUSD'.
        bar_datetime - The timestamp of bar based on which signal was generated
        datetime - The timestamp at which the signal was generated.
        signal_type - 'LONG' or 'SHORT'.
        strength - An adjustment factor "suggestion" used to scale quantity at the portfolio level.
            Useful for pairs strategies.
        stop_loss - The price where the order is closed at market automatically with loss.
        take_profit - The price where the order is closed at market automatically with profit.
        trade_id_to_exit - Trade to exit
        """

        super().__init__('SIGNAL', symbol)

        self.strategy_id = strategy_id
        self.bar_datetime = bar_datetime
        self.datetime = datetime
        self.signal_type = signal_type
        self.strength = strength
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.trade_id_to_exit = trade_id_to_exit

    def get_as_string(self):
        return ('Signal: StrategyId: %d, Symbol: %s, BarDatetime: %s, Datetime: %s, SignalType: %s, Strength: %d,' +
                ' StopLoss=%f, TakeProfit=%f, TradeIdToExit=%d') % \
               (self.strategy_id, self.symbol, self.bar_datetime, self.datetime, self.signal_type, self.strength,
                self.get_zero_if_none_or_value(self.stop_loss), self.get_zero_if_none_or_value(self.take_profit),
                self.get_zero_if_none_or_value(self.trade_id_to_exit))

    def get_zero_if_none_or_value(self, value):
        if value is None:
            return 0
        else:
            return value
