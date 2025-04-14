from loguru import logger
from web3 import AsyncWeb3
import data.models
import settings
from client import Client


class RuBic:
    def __init__(self, client: Client):
        self.client = client

    async def swap_mon_to_wmon(self):
        wrap_mon = self.client.w3.eth.contract(
            address=AsyncWeb3.to_checksum_address('0x760AfE86e5de5fa0Ee542fc7B7B713e1c5425701'),
            abi=data.models.AbIs.wrap_monad
        )

        try:
            logger.info(
                f'Profile: {self.client.profile} {self.client.account.address} Swap MON to WMON')
            tx = await self.client.send_transaction(
                to=wrap_mon.address,
                data=wrap_mon.encode_abi('deposit', args=()),
                value=settings.RANGE_SWAP,

            )

            if tx:
                try:
                    await self.client.verif_tx(tx_hash=tx)
                    logger.success(
                        f'Profile: {self.client.profile} {self.client.account.address} Transaction success!! tx_hash: 0x{tx.hex()}')
                except Exception as err:
                    logger.warning(
                        f'Profile: {self.client.profile} {self.client.account.address} Transaction error!! tx_hash: 0x{tx.hex()}; error: {err}')
                    raise ValueError(f'{self.client.profile} Error transaction')
            else:
                logger.error(
                    f'Profile: {self.client.profile} {self.client.account.address} Transaction error!!!')
                raise ValueError(f'{self.client.profile} Error transaction')
        except Exception as er:
            logger.error(
                f'Profile: {self.client.profile} {self.client.account.address} {er}')
