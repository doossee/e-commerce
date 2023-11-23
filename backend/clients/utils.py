import logging

logger = logging.getLogger(__name__)

from drfpasswordless.settings import api_settings

def send_sms_with_callback_token(user, mobile_token, **kwargs):
    """
    Sends a SMS to user.mobile via Twilio.

    Passes silently without sending in test environment.
    """
    if api_settings.PASSWORDLESS_TEST_SUPPRESSION is True:
        # we assume success to prevent spamming SMS during testing.

        # even if you have suppression on– you must provide a number if you have mobile selected.
        if api_settings.PASSWORDLESS_MOBILE_NOREPLY_NUMBER is None:
            return False
            
        return True
    
    base_string = kwargs.get('mobile_message', api_settings.PASSWORDLESS_MOBILE_MESSAGE)

    try:
        if not api_settings.PASSWORDLESS_MOBILE_NOREPLY_NUMBER:
            # We need a sending number to send properly

            from eskiz_sms import EskizSMS
            eskiz = EskizSMS(
                'doossee.me@gmail.com',
                'V2gADtpVSPTCuIbAPKYtaHylyTtS0ZRXuNBmxR8Y',
                save_token=True,
                env_file_path='.env'
            )
            to_number = getattr(user, api_settings.PASSWORDLESS_USER_MOBILE_FIELD_NAME)
            if to_number.__class__.__name__ == 'PhoneNumber':
                to_number = to_number.__str__()

            response = eskiz.send_sms(
                mobile_phone=to_number,
                message=base_string % mobile_token.key
            )  
            return True
        else:
            logger.debug("Failed to send token sms. Missing PASSWORDLESS_MOBILE_NOREPLY_NUMBER.")
            return False
    except ImportError:
        logger.debug("Couldn't import Twilio client. Is twilio installed?")
        return False
    except KeyError:
        logger.debug("Couldn't send SMS."
                  "Did you set your Twilio account tokens and specify a PASSWORDLESS_MOBILE_NOREPLY_NUMBER?")
    except Exception as e:
        logger.debug("Failed to send token SMS to user: {}. "
                  "Possibly no mobile number on user object or the twilio package isn't set up yet. "
                  "Number entered was {}".format(user.id, getattr(user, api_settings.PASSWORDLESS_USER_MOBILE_FIELD_NAME)))
        logger.debug(e)
        return False