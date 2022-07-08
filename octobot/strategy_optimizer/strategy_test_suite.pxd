cimport octobot.backtesting as octobot_backtesting
cimport octobot.strategy_optimizer as strategy_optimizer


cdef class StrategyTestSuite(octobot_backtesting.AbstractBacktestingTest):
    cdef list _profitability_results
    cdef list _trades_counts

    cdef public double current_progress
    cdef public list exceptions
    cdef public list evaluators

    cpdef strategy_optimizer.TestSuiteResult get_test_suite_result(self)
